# 1
def length_is_valid(user: str) -> bool:
    if 3 <= len(user) <= 16:
        return True
    return False


def characters_are_valid(user: str) -> bool:
    for character in user:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True


def no_redundant_symbols(user: str) -> bool:
    if " " in user:
        return False
    return True


def username_is_valid(username_: str) -> bool:
    if length_is_valid(username_) and \
            characters_are_valid(username_) and \
            no_redundant_symbols(username_):
        return True
    return False


usernames = input().split(", ")
for username in usernames:
    if username_is_valid(username):
        print(username)

