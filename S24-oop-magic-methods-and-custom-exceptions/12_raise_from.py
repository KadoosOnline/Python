# When you translate a low-level error into your own one, keep the original:
# 'raise ... from e' records the cause and shows both in the traceback.
class ConfigError(Exception):
    'The configuration could not be read.'


def read_port(path: str) -> int:
    try:
        with open(path, encoding='utf-8') as f:
            return int(f.read().strip())
    except FileNotFoundError as e:
        raise ConfigError(f'{path} is missing') from e
    except ValueError as e:
        raise ConfigError(f'{path} does not contain a number') from e


if __name__ == '__main__':
    try:
        read_port('nothing.cfg')
    except ConfigError as e:
        print('Error:', e)
        print('Caused by:', repr(e.__cause__))

    # 'raise ... from None' hides the original cause, when it would only
    # confuse the user.
    try:
        try:
            int('abc')
        except ValueError:
            raise ConfigError('bad configuration') from None
    except ConfigError as e:
        print('Error:', e, '| cause:', e.__cause__)
