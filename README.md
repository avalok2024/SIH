# Basic Chatbot

This is a simple chatbot implemented in Python. It responds to predefined user queries using `if-else` statements and runs in a loop to continuously interact with the user until they decide to exit the conversation.

## Features
- The chatbot can respond to basic questions such as:
  - Greetings ("hello")
  - Questions about its name, age, and creator
  - Telling a joke
  - Discussing general topics like time, weather, and food
  - Providing help with the chatbot's capabilities
- It handles unrecognized queries by responding with a fallback message.
- The chatbot exits the conversation when the user types "bye."

## How It Works
1. **`process_input()`**: This function takes the user input and checks it against a series of predefined questions using `if-else` statements.
2. **Loop**: The main program runs in a loop, allowing the user to continuously interact with the chatbot until they decide to quit by typing "bye."

### Example Interaction
