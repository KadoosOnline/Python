# 'raise' creates an exception ourselves. It is how a function says
# "the value you gave me makes no sense".
def set_age(age: int) -> int:
    if age < 0:
        raise ValueError("Age can't be negative!")
    if age > 130:
        raise ValueError('Age is unrealistic!')
    return age


try:
    set_age(-5)
except ValueError as e:
    print('Refused:', e)

# Re-raising after logging is a common pattern: we note the problem,
# but we let the caller decide what to do.
def read_config(path: str) -> str:
    try:
        with open(path, encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f'[warning] {path} is missing')
        raise            # send the same exception further up


try:
    read_config('nothing.cfg')
except FileNotFoundError:
    print('The caller handled it.')
