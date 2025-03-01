import nltk
from nltk.chat.util import Chat, reflections

# Define chatbot responses using pattern-response pairs
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hey there!", "Hi, how can I help you?"]],
    [r"how are you", ["I'm just a bot, but I'm doing fine!", "I'm good, thanks for asking!"]],
    [r"what is your name", ["I'm a chatbot! You can call me ChatBot."]],
    [r"(.*) your name", ["I am ChatBot, your virtual assistant!"]],
    [r"(.*) help (.*)", ["I'm here to help! What do you need?", "Tell me how I can assist you."]],
    [r"bye|goodbye", ["Goodbye! Have a great day!", "See you later!"]],
    [r"(.*)", ["I'm not sure I understand. Could you rephrase that?", "Can you clarify?"]]
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

def start_chat():
    print("Hello! I'm a chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print("ChatBot: Goodbye! Have a great day!")
            break
        response = chatbot.respond(user_input)
        print(f"ChatBot: {response}")

if __name__ == "__main__":
    start_chat()
