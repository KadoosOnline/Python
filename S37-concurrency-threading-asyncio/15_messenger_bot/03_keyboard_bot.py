'''Buttons: an inline keyboard and `CallbackQueryHandler`.

An inline keyboard is attached to a message. Every button carries a
`callback_data` string, and pressing it sends that string back to the bot --
it is not a new message from the user, it is a CALLBACK QUERY.

    keyboard = [[InlineKeyboardButton('Text', callback_data='value')], ...]
    await message.reply_text('Choose:', reply_markup=InlineKeyboardMarkup(keyboard))

Two rules:

1. **Always `await query.answer()`**, even when you show nothing. Until you
   do, the messenger keeps a little spinner on the button and the user thinks
   the bot is broken.
2. `callback_data` is limited to 64 bytes and comes back as an untrusted
   string. Treat it exactly like `input()`: check it before you use it. Never
   put a database id in it that a user could change to somebody else's.
'''

import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (Application, CallbackQueryHandler, CommandHandler,
                          ContextTypes)

from config import BASE_URL, get_token


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)
# httpx logs every single request at INFO level: far too noisy.
logging.getLogger('httpx').setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# The menu, as data. `callback_data` is the key, the text is what is shown.
MENU = {'python': 'Introduction to Python',
        'advanced': 'Advanced Python',
        'flask': 'Web development with Flask'}

PRICES = {'python': 4_500_000, 'advanced': 5_200_000, 'flask': 3_800_000}


def build_keyboard() -> InlineKeyboardMarkup:
    '''One button per course, one per row.'''
    rows = [[InlineKeyboardButton(title, callback_data=key)]
            for key, title in MENU.items()]
    rows.append([InlineKeyboardButton('Cancel', callback_data='cancel')])
    return InlineKeyboardMarkup(rows)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is None:
        return
    await update.message.reply_text('Which course interests you?',
                                    reply_markup=build_keyboard())


async def on_button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    '''Called when any button of the keyboard is pressed.'''
    query = update.callback_query
    if query is None:
        return

    # Rule 1: answer first, always.
    await query.answer()

    choice = query.data or ''

    if choice == 'cancel':
        await query.edit_message_text('No problem. Send /start again later.')
        return

    # Rule 2: never trust callback_data.
    if choice not in MENU:
        logger.warning('Unknown callback_data: %r', choice)
        await query.edit_message_text('I do not know that choice.')
        return

    await query.edit_message_text(
        f'{MENU[choice]}\nPrice: {PRICES[choice]:,} toman\n\n'
        'Send /start to choose again.')


def main() -> None:
    application = (Application.builder()
                   .token(get_token())
                   .base_url(BASE_URL)
                   .build())

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(on_button))

    print('The bot is running. Press Ctrl-C to stop it.')
    application.run_polling()


if __name__ == '__main__':
    main()
