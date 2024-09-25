# Function to process user queries.

def process_input(user_input):
    if "hello" in user_input.lower():
        return "Hello! How can I assist you today?"
    elif "name" in user_input.lower():
        return "I am a chatbot created to assist you with predefined answers."
    elif "age" in user_input.lower():
        return "I do not have an age, as I am a program."
    elif "creator" in user_input.lower():
        return "I was created by a developer like you!"
    elif "weather" in user_input.lower():
        return "Sorry, I don't have access to live weather data."
    elif "joke" in user_input.lower():
        return "Why don't programmers like nature? It has too many bugs!"
    elif "color" in user_input.lower():
        return "I don't see colors, but I imagine blue is calming."
    elif "time" in user_input.lower():
        return "I don't have access to the current time, but I hope it's a good one!"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day!"
    elif "help" in user_input.lower():
        return "You can ask me about my name, my creator, or just ask me for a joke!"
    elif "food" in user_input.lower():
        return "I don't eat, but I've heard pizza is a favorite!"
    elif "robot" in user_input.lower():
        return "Yes, I am a robot. A friendly one!"
    else:
        return "I'm sorry, I don't understand that. Could you ask something else?"

# Chatbot loop to handle user queries
def chatbot():
    print("Hello! I'm a basic chatbot. Ask me anything or type 'bye' to exit.")
    
    while True:
        user_input = input("You: ")
        if "bye" in user_input.lower():
            print("Chatbot: Goodbye! Have a nice day!")
            break
        response = process_input(user_input)
        print(f"Chatbot: {response}")

# Run the chatbot
chatbot()
