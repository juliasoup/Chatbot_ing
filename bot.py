from handlers.intent_handler import process_message

def chat_loop():
    print("Virtual sales assistant started! Type 'exit' to quit.")

    while True:
        user_input = input("Customer: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Assistant: It was a pleasure assisting you!")
            break

        response = process_message(user_input)
        print("Assistant:", response)


if __name__ == "__main__":
    chat_loop()
