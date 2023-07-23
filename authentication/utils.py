import re

EMAIL_REGEX=r"^[\w\-\.]+@([\w\-]+\.)+[\w\-]{2,4}$"
PASSWORD_REGEX=r"^(?=.*[A-Za-z])(?=.*[0-9])(?=.*[@$!%*#?&])[A-Za-z0-9@$!%*#?&]{8,}$"

def registrationValidation(username, password):
    re.compile(EMAIL_REGEX)
    if(not re.fullmatch(EMAIL_REGEX, username)): return [False, 'username']

    re.compile(PASSWORD_REGEX)
    if(not re.fullmatch(PASSWORD_REGEX, password)): return [False, 'password']

    return [True, '']