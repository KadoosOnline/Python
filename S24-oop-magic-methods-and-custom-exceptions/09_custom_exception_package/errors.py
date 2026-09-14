'''The exceptions of the application, kept in their own module.

Putting them apart means every module can import them without a circular
import problem.
'''


class LoginError(Exception):
    'Raised when a login attempt fails.'
