class NameTooShortError(Exception):
    """ Raised when name is short """
    pass

class MustContainAtSymbolError(Exception):
    """ Raised when there is no special symbol """
    pass

class InvalidDomainError(Exception):
    """ Raised when there is no valid domain """
    pass

VALID_DOMAINS = ('.com', '.bg', '.net', '.org')
EMAIL_MIN_LENGTH = 4

while (email := input()) != 'End':
    # checks if @ is in Email

    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain '@'.")

    # Splits email into name and domain

    name, domain = email.split('@')
    domain_extension = domain.split('.')[-1]

    # checks the name in the email is less than or equal to 4

    if len(name) <= EMAIL_MIN_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")

    # Checks if the domain is valid

    if f'.{domain_extension}' not in VALID_DOMAINS:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")
    # If there is no error messages printing the needed result
    print('Email is valid')

