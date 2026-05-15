import tkinter as tk

def send_message():
    user_message = entry.get().lower()

    if user_message == "hello":
        response = "Hi! How can I help you?"
    elif user_message == "what is ai":
        response = "AI means Artificial Intelligence."
    elif user_message == "bye":
        response = "Goodbye!"
    else:
        response = "Sorry, I don't understand."

    chat.insert(tk.END, "You: " + user_message + "\n")
    chat.insert(tk.END, "Bot: " + response + "\n\n")

    entry.delete(0, tk.END)

root = tk.Tk()
root.title("FAQ Chatbot")

chat = tk.Text(root, height=15, width=50)
chat.pack()

entry = tk.Entry(root, width=40)
entry.pack()

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack()

root.mainloop()