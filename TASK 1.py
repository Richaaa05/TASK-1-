#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Richa Sanka
#
# Created:     25-05-2024
# Copyright:   (c) Richa Sanka 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Define a function to handle the responses
def chatbot_response(user_input):
    # Convert user input to lowercase for easier matching
    user_input = user_input.lower()

    # Define responses based on if-else conditions
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm doing good! How about you?"
    elif "Can you help me out with my work" in user_input:
        return "yes sure."
    elif "okay then bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a nice day!"
    else:
        return "I'm sorry, I didn't understand that."

# Main loop to interact with the chatbot
print("Type 'bye' or 'exit' to end the chat")
while True:
    user_input = input("You: ")
    if "bye" in user_input.lower() or "exit" in user_input.lower():
        print("Bot: Goodbye! Have a nice day!")
        break
    response = chatbot_response(user_input)
    print("Bot:", response)




