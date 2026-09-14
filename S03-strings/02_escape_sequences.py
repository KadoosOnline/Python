# A backslash starts an "escape sequence": a special character written with
# ordinary letters.
print('Hello\nKadoos!')     # \n  -> new line
print('1\t2\t3')            # \t  -> tab
print('I\'m a student')     # \'  -> a single quote inside single quotes
print("\"\"\"")             # \"  -> a double quote inside double quotes
print('C:\\windows')        # \\  -> one real backslash

# A raw string (r'...') switches escaping off - very handy for Windows paths.
print(r'C:\windows\system32')
