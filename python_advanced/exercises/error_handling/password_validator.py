import re
class PasswordTooShortError(Exception):
    """ Raised when password is not at least 8 characters long """
    pass

class PasswordTooCommonError(Exception):
    """ Raised when password consists of only digits, only letters, or only special characters """
    pass

class PasswordNoSpecialCharactersError(Exception):
    """ Raised when password not have at least 1 special character """
    pass

class PasswordContainsSpacesError(Exception):
    """ Raised when IS empty space in password """
    pass

VALID_PASSWORD_PATTERN = r"^(?=.*[@*&%])(?!^[A-Za-z]+$)(?!^\d+$)(?!^[@*&%]+$)(?!.*\s).{8,}$"


while (password := input()) != 'Done':
    if not re.match(VALID_PASSWORD_PATTERN, password):
        # check password if is least 8 characters long
        if len(password) < 8:
            raise PasswordTooShortError("Password must contain at least 8 characters")

        # checks password if only digits, only letters, or only special characters
        if re.fullmatch(r"[A-Za-z]+", password) or re.fullmatch(r"\d+", password) or re.fullmatch(r"[@*&%]+", password):
            raise PasswordTooCommonError("Password must be a combination of digits, letters, and special characters")

        # checks if password contains special characters
        if not re.search(r"[@*&%]", password):
            raise PasswordNoSpecialCharactersError("Password must contain at least 1 special character")

        # checks if password has empty spaces:
        if re.search(r"\s", password):
            raise PasswordContainsSpacesError("Password must not contain spaces.")
    else:
        print("Password is valid")



