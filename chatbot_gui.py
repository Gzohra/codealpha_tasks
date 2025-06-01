import tkinter as tk
from tkinter import scrolledtext
import random
import time

def get_response(user_input):
    user_input = user_input.lower().strip()

    responses = {
        "hello": ["Hi there! ", "Hello! How can I assist you?", "Hey! What's up?"],
        "hi": ["Hello! How can I assist you?", "Hi! Need any help?", "Hey! How are you?"],
        "how are you": ["I'm just a bot, but I'm doing great! ", "Doing well, thanks!", "I'm fine, how about you?"],
        "what is your name": ["I'm CodeAlphaBot, your Python chatbot.", "You can call me CodeAlphaBot."],
        "bye": ["Goodbye! Have a great day! ", "See you later!", "Bye! Take care!"],
        "help": ["Try asking: 'hello', 'how are you', or 'bye'.", "You can say hi or ask my name!"]
    }

    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return "Sorry, I didn't understand that. "

def get_timestamp():
    return time.strftime("[%I:%M %p] ")

def send_message():
    msg = user_entry.get()
    if msg.strip() == "":
        return

    timestamp = get_timestamp()
    chat_area.config(state=tk.NORMAL)
    chat_area.insert(tk.END, timestamp + "You: " + msg + "\n")
    
    reply = get_response(msg)
    bot_time = get_timestamp()
    chat_area.insert(tk.END, bot_time + "Bot: " + reply + "\n\n")
    
    chat_area.config(state=tk.DISABLED)
    user_entry.delete(0, tk.END)
    chat_area.yview(tk.END)

def send_message_event(event):
    send_message()

def clear_chat():
    chat_area.config(state=tk.NORMAL)
    chat_area.delete(1.0, tk.END)
    chat_area.insert(tk.END, get_timestamp() + "Bot: Hello! I'm CodeAlphaBot. Type 'help' to get started.\n\n")
    chat_area.config(state=tk.DISABLED)

# Root Window
root = tk.Tk()
root.title(" CodeAlpha Chatbot")
root.geometry("420x550")
root.configure(bg="#d6eaf8")  

# Chat Area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12), bg="white", fg="black", bd=2, relief="sunken")
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_area.insert(tk.END, get_timestamp() + "Bot: Hello! I'm CodeAlphaBot. Type 'help' to get started.\n\n")
chat_area.config(state=tk.DISABLED)

# User Entry Field 
user_entry = tk.Entry(root, font=("Arial", 14), bg="#ECEBE7", fg="black", bd=2, relief="solid", insertbackground="black")
user_entry.pack(padx=10, pady=(0,10), fill=tk.X)
user_entry.bind("<Return>", send_message_event)

# Buttons Frame
frame_buttons = tk.Frame(root, bg="#dfdce6")
frame_buttons.pack(pady=(0, 10))

send_button = tk.Button(frame_buttons, text="Send", font=("Arial", 12), command=send_message, bg="#3ca1e5", fg="white", activebackground="#a5b4bd")
send_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(frame_buttons, text="Clear Chat", font=("Arial", 12), command=clear_chat, bg="#EF5353", fg="black", activebackground="#64A1D4")
clear_button.grid(row=0, column=1, padx=5)

root.mainloop()

