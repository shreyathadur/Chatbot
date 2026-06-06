from datetime import datetime
import random

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the computer cold? It forgot to close Windows.",
    "Why did the programmer quit his job? Because he didn't get arrays.",
    "Debugging is like being a detective in a crime movie where you're also the murderer."
]

def show_help():
    print("\nAvailable Commands:")
    print("- hello")
    print("- how are you")
    print("- what is your name")
    print("- who created you")
    print("- date")
    print("- time")
    print("- joke")
    print("- weather")
    print("- calc <expression>")
    print("- help")
    print("- bye\n")

def chatbot():
    print("=" * 50)
    print("Welcome to Smart Basic Chatbot")
    print("Type 'help' to see available commands")
    print("Type 'bye' to exit")
    print("=" * 50)

    while True:
        user = input("\nYou: ").strip().lower()

        if user == "hello":
            print("Bot: Hi! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm doing great. Thanks for asking!")

        elif user == "what is your name":
            print("Bot: My name is Smart Basic Chatbot.")

        elif user == "who created you":
            print("Bot: I was created using Python.")

        elif user == "date":
            current_date = datetime.now().strftime("%d-%m-%Y")
            print(f"Bot: Today's date is {current_date}")

        elif user == "time":
            current_time = datetime.now().strftime("%I:%M:%S %p")
            print(f"Bot: Current time is {current_time}")

        elif user == "joke":
            print("Bot:", random.choice(jokes))

        elif user == "weather":
            city = input("Enter city name: ")
            print(f"Bot: Weather information for {city} is currently unavailable.")

        elif user.startswith("calc"):
            try:
                expression = user.replace("calc", "").strip()
                result = eval(expression)
                print(f"Bot: Result = {result}")
            except:
                print("Bot: Invalid calculation.")

        elif user == "help":
            show_help()

        elif user == "bye":
            print("Bot: Goodbye! Have a wonderful day.")
            break

        else:
            print("Bot: Sorry, I don't understand that command.")

if __name__ == "__main__":
    chatbot()