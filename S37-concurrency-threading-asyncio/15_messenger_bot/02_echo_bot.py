'''Answering ordinary messages: `MessageHandler` and filters.

`CommandHandler` only sees messages that start with `/`. Everything else goes
to a `MessageHandler`, and a FILTER says which messages it wants:

    filters.TEXT                    any text
    filters.TEXT & ~filters.COMMAND text that is not a command
    filters.PHOTO                   photos
    filters.Document.ALL            any file
    filters.User(user_id=...)       only from one person

The operators are `&` (and), `|` (or) and `~` (not) -- exactly like the
comparison filters of a database query.

ORDER MATTERS: the handlers are tried in the order they were added, and the
first one that matches wins. Put the specific handlers before the general
ones, or your echo handler will swallow everything.
'''

from telegram import Update
from telegram.ext import (Application, CommandHandler, ContextTypes,
                          MessageHandler, filters)

from config import BASE_URL, get_token


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is None:
        return
    await update.message.reply_text(
        'Send me anything and I will send it back.\n'
        'Try the word "kadoos".')


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    '''Send the same text back, with one special case.'''
    if update.message is None or update.message.text is None:
        return

    text = update.message.text
    if text.strip().lower() == 'kadoos':
        await update.message.reply_text('Welcome to Kadoos Institute!')
        return

    await update.message.reply_text(text)


async def on_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is None:
        return
    await update.message.reply_text('A nice picture!')


async def on_error(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
    '''Called for every exception raised in a handler.

    Without this, an exception in a handler is logged and the user gets
    nothing at all -- the bot simply looks broken.
    '''
    print(f'Error while handling an update: {context.error}')


def main() -> None:
    application = (Application.builder()
                   .token(get_token())
                   .base_url(BASE_URL)
                   .build())

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.PHOTO, on_photo))
    # The general handler goes LAST.
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    application.add_error_handler(on_error)

    print('The bot is running. Press Ctrl-C to stop it.')
    application.run_polling()


if __name__ == '__main__':
    main()
