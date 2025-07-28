import re


text = input()


email_pattern = r"(^|(?<=\s))(([a-zA-Z0-9]+)([\.\-_]?)([A-Za-z0-9]+)(@)([a-zA-Z]+([\.\-_][A-Za-z]+)+))(\b|(?=\s))"


emails = re.finditer(email_pattern, text)

for email in emails:
    print(email.group(2))