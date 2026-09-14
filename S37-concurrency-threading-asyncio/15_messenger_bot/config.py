'''Where the bot reads its token -- and why it is not written here.

*** NEVER put a token, a password or an API key in a source file. ***

A token is a password: whoever has it controls your bot completely. Once it is
written in a file it ends up in a backup, in a zip you send to a friend, in a
GitHub repository -- and it stays in the history of that repository even after
you delete the line. (The first version of this course did exactly that: a
live bot token was committed in `constants.py`. If that ever happens to you,
the only real fix is to REVOKE the token and get a new one.)

The token belongs in an ENVIRONMENT VARIABLE instead:

    Windows (PowerShell, for this window only)
        $env:BOT_TOKEN = "123456:AbCdEf..."
    Windows (cmd)
        set BOT_TOKEN=123456:AbCdEf...
    Linux / macOS
        export BOT_TOKEN="123456:AbCdEf..."

Then `python 01_hello_bot.py`.

For a real project, use a `.env` file plus `python-dotenv` -- and put `.env`
in `.gitignore` on the very first day.
'''

import os


# Bale uses the same API as Telegram, at a different address.
# For Telegram itself, leave BOT_BASE_URL unset.
BASE_URL = os.environ.get('BOT_BASE_URL', 'https://tapi.bale.ai/')


def get_token() -> str:
    '''Read the token, or explain clearly what is missing.'''
    token = os.environ.get('BOT_TOKEN')
    if not token:
        raise SystemExit(
            'BOT_TOKEN is not set.\n\n'
            '  Windows : set BOT_TOKEN=your-token-here\n'
            '  Linux   : export BOT_TOKEN="your-token-here"\n\n'
            'Get a token from @BotFather (Telegram) or @BotFather (Bale).')
    return token
