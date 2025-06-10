import tkinter as tk

# Function to handle sending messages
def send_message():
    user_input = entry.get().lower()
    chat_log.insert(tk.END, "You: " + user_input + "\n")
    entry.delete(0, tk.END)

    if user_input == "hello":
        response = "Hi!"
    elif user_input == "how are you":
        response = "I'm fine, thanks!"
    elif user_input == "bye":
        response = "Goodbye!"
    else:
        response = "I don't understand that."

    chat_log.insert(tk.END, "Bot: " + response + "\n")

# GUI setup
window = tk.Tk()
window.title("Simple ChatBot")

chat_log = tk.Text(window, height=20, width=50)
chat_log.pack(pady=10)

entry = tk.Entry(window, width=40)
entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(side=tk.LEFT, padx=(5, 10), pady=(0, 10))

window.mainloop()
