class Email:
    def __init__(self , sender : str , receiver : str, content : str, is_sent = False):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = is_sent

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

emails = []

line = input()
while line != 'Stop':
    current_line = line.split()
    current_sender = current_line[0]
    current_receiver = current_line[1]
    current_content = current_line[2]

    email = Email(current_sender , current_receiver , current_content)
    emails.append(email)
    line = input()

send_emails = list(map(lambda x: int(x), input().split(', ')))

for x in send_emails:
    emails[x].send()

for email in emails:
    print(email.get_info())