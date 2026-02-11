messages_history = []

def get_messages():
    return messages_history

def add_message(messages):
    global messages_history
    messages_history = messages