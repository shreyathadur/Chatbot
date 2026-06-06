import tkinter as tk
from datetime import datetime
import random

jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why was the computer cold? It forgot to close Windows.",
    "Debugging is like being a detective in a crime movie."
]

def get_response(user):
    user = user.lower()

    if user == "hello":
        return "Hi! Nice to meet you."

    elif user == "how are you":
        return "I'm doing great. Thanks for asking!"

    elif user == "time":
        return datetime.now().strftime("%I:%M:%S %p")

    elif user == "date":
        return datetime.now().strftime("%d-%m-%Y")

    elif user == "joke":
        return random.choice(jokes)

    elif user == "what is your name":
        return "My name is Smart Basic Chatbot."

    elif user == "bye":
        return "Goodbye!"

    else:
        return "Sorry, I don't understand."

def send_message():
    user = entry.get()

    if not user.strip():
        return

    chat_box.insert(tk.END, f"You: {user}\n")

    response = get_response(user)

    chat_box.insert(tk.END, f"Bot: {response}\n\n")

    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Smart Basic Chatbot")
root.geometry("600x500")

chat_box = tk.Text(root, height=20, width=70)
chat_box.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=5)

send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack()

root.mainloop()