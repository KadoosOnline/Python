'''Receiving and sending files.

    file = await document.get_file()       # ask the server for the file
    await file.download_to_drive(path)     # download it

Both are `await`ed: they are network calls.

SECURITY -- the reason this example is longer than the original one:

`document.file_name` is chosen by whoever sends the file. A file called
`../../passwords.txt` would be written OUTSIDE your download folder. That
attack is called "path traversal", and the defence is to keep only the last
part of the name (`Path(name).name`) and to check the final path really is
inside the folder you meant.

Also check the SIZE before downloading; a bot with no limit is an easy way to
fill somebody's disk.
'''

import re
from pathlib import Path

from telegram import Update
from telegram.ext import (Application, CommandHandler, ContextTypes,
                          MessageHandler, filters)

from config import BASE_URL, get_token


DOWNLOAD_DIR = Path(__file__).parent / 'downloads'
DOWNLOAD_DIR.mkdir(exist_ok=True)

MAX_SIZE = 5 * 1024 * 1024          # 5 MB


def safe_filename(name: str) -> str:
    '''Turn a name chosen by a stranger into a name we can safely write.'''
    # Path(...).name drops every folder: '../../etc/passwd' -> 'passwd'
    name = Path(name).name
    # Then keep only harmless characters.
    name = re.sub(r'[^A-Za-z0-9._-]', '_', name)
    # '.' and '..' survive both steps above and are not file names at all.
    if name in {'', '.', '..'}:
        return 'file.bin'
    return name


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is None:
        return
    await update.message.reply_text(
        f'Send me a file (up to {MAX_SIZE // 1024 // 1024} MB) '
        'and I will save it.')


async def on_document(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = update.message
    if message is None or message.document is None:
        return

    document = message.document

    if document.file_size and document.file_size > MAX_SIZE:
        await message.reply_text('That file is too big for me.')
        return

    filename = safe_filename(document.file_name or f'{document.file_id}.bin')
    destination = DOWNLOAD_DIR / filename

    # Belt and braces: make sure we really stay inside the folder.
    if DOWNLOAD_DIR.resolve() not in destination.resolve().parents:
        await message.reply_text('I do not like that file name.')
        return

    telegram_file = await document.get_file()
    await telegram_file.download_to_drive(custom_path=destination)

    await message.reply_text(f'Saved as {filename} '
                             f'({destination.stat().st_size} bytes).')


async def send_back(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    '''/last sends the most recently saved file back.'''
    if update.message is None:
        return
    files = sorted(DOWNLOAD_DIR.iterdir(), key=lambda p: p.stat().st_mtime)
    if not files:
        await update.message.reply_text('I have nothing yet.')
        return
    # `with` closes the file even if the upload fails.
    with open(files[-1], 'rb') as file:
        await update.message.reply_document(file, filename=files[-1].name)


def main() -> None:
    application = (Application.builder()
                   .token(get_token())
                   .base_url(BASE_URL)
                   .build())

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('last', send_back))
    application.add_handler(
        MessageHandler(filters.Document.ALL, on_document))

    print('The bot is running. Press Ctrl-C to stop it.')
    application.run_polling()


if __name__ == '__main__':
    main()
