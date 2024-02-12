def show_messages(messages):
    """Print all messages in the list"""
    for message in messages:
        print(message)


def send_messages(messages, sent_messages):
    """Print each message, and then move it to sent_messages"""
    print("\nSending all the messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)


messages = ['hi there!', 'whazzup!', 'howdy?']
show_messages(messages)

sent_messages = []
send_messages(messages, sent_messages)

print("\nFinal lists:")
print(messages)
print(sent_messages)
