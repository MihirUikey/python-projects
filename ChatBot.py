import nltk
from nltk.chat.util import Chat, reflections

#creating a list of patterns and responses for the chatbot
patterns = [
    (r"hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"how are you?", ["I'm doing well, thank you!", "I'm fine, thanks for asking."]),
    (r"what's your name?", ["You can call me alen.", "I'm alen, nice to meet you!"]),
    (r"what can you do\?", ["I can answer basic questions and engage in a conversation."]),
    (r"what time is it?", ["It's time for you to get a watch!", "Time for you to upgrade to a smartwatch!"]),
    (r"where are you from?", ["I'm from the digital world!", "I exist in the realm of code."]),
    (r"tell me a joke", ["Why don't scientists trust atoms? Because they make up everything!"]),
    (r"how old are you?", ["I'm as old as the internet, eternal and ever-learning!"]),
    (r"quit|exit", ["Goodbye!", "Bye!", "See you later!"]),
]

#creating chat object with the patterns and reflections
chatbot = Chat(patterns, reflections)

#function to start the conversation with the chatbot
def start_chat():
    print("Welcome to the alen. How can I assist you today?")
    while True:
        user_input = input("You: ")
        response = chatbot.respond(user_input)
        print("ChatBot:", response)
        if user_input.lower() in ["quit", "exit"]:
            break

#calling the main function to start a chat session
if __name__ == "__main__":
    start_chat()
