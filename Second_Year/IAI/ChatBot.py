import random

def get_response(user_input):
    responses = {
        "hi": "Hello, how are you?",
        "how are you?": "I'm doing well, thank you.",
        "what's your name?": "My name is Chatbot.",
        "bye": "Goodbye, take care!",
        "default": "I'm sorry, I don't understand. Can you please rephrase your question?"
    }

    if user_input.lower() in responses:
        return responses[user_input.lower()]
    else:
        return responses["default"]

print("Hello! I'm a chatbot. How can I help you?")
while True:
    user_input = input("> ")
    if user_input.lower() == "exit":
        break
    response = get_response(user_input)
    print(response)