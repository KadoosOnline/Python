'''The project: a quiz bot that remembers where each player is.

A bot talks to many people at the same time, and every one of them is in the
middle of their own conversation. So the state CANNOT live in a global
variable -- that would mix all the players together.

`python-telegram-bot` gives every chat its own storage:

    context.user_data   a dict, private to one user
    context.chat_data   a dict, shared by everyone in one group
    context.bot_data    a dict, shared by the whole bot

They are ordinary dictionaries. (They live in memory: restarting the bot
forgets everything. A real bot uses `PicklePersistence`, or SQLite -- session
31 -- to survive a restart.)

The bot is entirely asynchronous: hundreds of players can be answering at the
same moment, in ONE thread, because every `await` gives the others a turn.
'''

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (Application, CallbackQueryHandler, CommandHandler,
                          ContextTypes)

from config import BASE_URL, get_token


QUESTIONS = [
    {'text': 'Which keyword defines a function in Python?',
     'options': ['def', 'function', 'fun'], 'answer': 0},
    {'text': 'What does len("Kadoos") return?',
     'options': ['5', '6', '7'], 'answer': 1},
    {'text': 'Which type CANNOT be changed after it is created?',
     'options': ['list', 'dict', 'tuple'], 'answer': 2},
    {'text': 'What does 7 // 2 give?',
     'options': ['3.5', '3', '4'], 'answer': 1},
    {'text': 'Which library draws windows and is in the standard library?',
     'options': ['PySide6', 'tkinter', 'flask'], 'answer': 1},
]


def question_keyboard(index: int) -> InlineKeyboardMarkup:
    '''Buttons for one question. callback_data is "questionindex:choice".'''
    question = QUESTIONS[index]
    rows = [[InlineKeyboardButton(option, callback_data=f'{index}:{number}')]
            for number, option in enumerate(question['options'])]
    return InlineKeyboardMarkup(rows)


async def send_question(message, context: ContextTypes.DEFAULT_TYPE) -> None:
    '''Send the question the player is currently on, or the final score.'''
    index = context.user_data['index']

    if index >= len(QUESTIONS):
        score = context.user_data['score']
        total = len(QUESTIONS)
        await message.reply_text(
            f'Finished! Your score: {score}/{total}\n'
            + ('Excellent!' if score == total else 'Send /start to try again.'))
        return

    await message.reply_text(
        f'Question {index + 1}/{len(QUESTIONS)}\n\n{QUESTIONS[index]["text"]}',
        reply_markup=question_keyboard(index))


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    '''/start -- begin a new quiz for THIS user.'''
    if update.message is None or context.user_data is None:
        return
    context.user_data['index'] = 0
    context.user_data['score'] = 0
    await update.message.reply_text('Let us start the quiz!')
    await send_question(update.message, context)


async def on_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    '''A button was pressed.'''
    query = update.callback_query
    if query is None or context.user_data is None:
        return
    await query.answer()

    # The player may have pressed a button of an old game after a restart.
    if 'index' not in context.user_data:
        await query.edit_message_text('Send /start to begin.')
        return

    # callback_data comes from outside: parse it defensively.
    try:
        question_index, choice = (int(part) for part in (query.data or '').split(':'))
    except ValueError:
        await query.edit_message_text('I did not understand that answer.')
        return

    # Ignore a button from a question the player has already left behind
    # (they can scroll up and press an old one).
    if question_index != context.user_data['index']:
        return          # already answered at the top of this function

    question = QUESTIONS[question_index]
    correct = choice == question['answer']
    if correct:
        context.user_data['score'] += 1

    right_answer = question['options'][question['answer']]
    await query.edit_message_text(
        f'{question["text"]}\n\n'
        + ('Correct!' if correct else f'No -- the answer was "{right_answer}".'))

    context.user_data['index'] += 1
    await send_question(query.message, context)


async def score(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    '''/score -- where am I?'''
    if update.message is None or context.user_data is None:
        return
    if 'score' not in context.user_data:
        await update.message.reply_text('You have not started yet. Send /start.')
        return
    await update.message.reply_text(
        f'{context.user_data["score"]} correct, '
        f'question {context.user_data["index"] + 1} of {len(QUESTIONS)}.')


def main() -> None:
    application = (Application.builder()
                   .token(get_token())
                   .base_url(BASE_URL)
                   .build())

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('score', score))
    application.add_handler(CallbackQueryHandler(on_answer))

    print('The quiz bot is running. Press Ctrl-C to stop it.')
    application.run_polling()


if __name__ == '__main__':
    main()
