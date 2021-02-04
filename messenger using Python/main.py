



import time

db = [
    {
        'text': 'Hi',
        'time': time.time(),
        'name': 'Nick'
    },
    {
        'text': 'Hello, Nick',
        'time': time.time(),
        'name': 'Jane'
    }
]

def print_message(message):
    # TODO beautify time
    print(message['time'], message['name'])
    print(message['text'])
    print()

def print_messages(db):
    for message in db:
        print_message(message)

def send_message(name, text):
    message = {
        'text': text,
        'time': time.time(),
        'name': name
    }
    db.append(message)

def get_messages(after):
    messages = []
    for message in db:
        if message['time'] > after:
            messages.append(message)
    return messages






