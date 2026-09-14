'''The first bot: one command, one answer.

`python-telegram-bot` is entirely built on asyncio -- which is why this
session ends here. Every handler is an `async def`, and every call to the
network is `await`ed. The library runs the event loop for you: you never call
`asyncio.run()` yourself.

    pip install python-telegram-bot

The shape of every bot:

    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler('hello', hello))
    application.run_polling()

`run_polling()` asks the server "anything new?" in a loop, for ever. Stop it
with Ctrl-C. (The other way, `run_webhook()`, needs a public server: the
messenger calls YOU.)

Two handler arguments, always the same:
    update    what happened (the message, who sent it...)
    context   the tools: the bot, the arguments, the stored data
'''

from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from config import BASE_URL, get_token


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    '''Answers /hello.'''
    # update.message CAN be None (an edited message, a channel post...), so
    # check instead of silencing the type checker with a `# type: ignore`.
    if update.message is None or update.effective_user is None:
        return
    name = update.effective_user.first_name
    await update.message.reply_text(f'Hello {name}! Welcome to Kadoos.')


async def dice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    '''Answers /dice with a random number.

    Note the name: calling this function `random` -- as the first version of
    this course did -- would shadow the `random` module for the whole file.
    '''
    import random as random_module

    if update.message is None:
        return
    await update.message.reply_text(f'You rolled {random_module.randint(1, 6)}')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message is None:
        return
    await update.message.reply_text('Commands: /hello, /dice, /help')


def main() -> None:
    # `.base_url(...)` is what makes the same library talk to Bale.
    # Remove that line to use Telegram.
    application = (Application.builder()
                   .token(get_token())
                   .base_url(BASE_URL)
                   .build())

    application.add_handler(CommandHandler('hello', hello))
    application.add_handler(CommandHandler('dice', dice))
    application.add_handler(CommandHandler('help', help_command))

    print('The bot is running. Press Ctrl-C to stop it.')
    application.run_polling()


# The main guard matters here: without it, importing this file would start the
# bot. The first version of this course built the application at module level.
if __name__ == '__main__':
    main()
