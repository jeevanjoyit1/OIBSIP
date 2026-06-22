import socket
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext

HOST = "127.0.0.1"
PORT = 55555

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

root = tk.Tk()
root.title("Chat Application")
root.geometry("700x500")
root.configure(bg="#2C3E50")

username = simpledialog.askstring("Username", "Enter your username:")

chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    bg="white",
    fg="black",
    font=("Arial", 11)
)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

chat_area.tag_config("self", foreground="blue")
chat_area.tag_config("other", foreground="green")
chat_area.tag_config("server", foreground="red")

bottom_frame = tk.Frame(root, bg="#2C3E50")
bottom_frame.pack(fill=tk.X, padx=10, pady=5)

message_entry = tk.Entry(
    bottom_frame,
    font=("Arial", 12)
)
message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

send_button = tk.Button(
    bottom_frame,
    text="Send",
    bg="#27AE60",
    fg="white",
    font=("Arial", 10, "bold")
)
send_button.pack(side=tk.RIGHT)

emoji_frame = tk.Frame(root, bg="#2C3E50")
emoji_frame.pack(pady=5)

emojis = ["😀", "😂", "😍", "👍", "❤️", "🔥", "🎉"]


def add_emoji(emoji):
    message_entry.insert(tk.END, emoji)


for emoji in emojis:
    btn = tk.Button(
        emoji_frame,
        text=emoji,
        command=lambda e=emoji: add_emoji(e),
        font=("Arial", 12)
    )
    btn.pack(side=tk.LEFT, padx=2)


def write():
    message = message_entry.get()

    if message.strip():
        full_message = f"{username}: {message}"
        client.send(full_message.encode())

    message_entry.delete(0, tk.END)


send_button.config(command=write)


def receive():
    while True:
        try:
            message = client.recv(1024).decode()

            if message == "USERNAME":
                client.send(username.encode())

            else:
                chat_area.config(state=tk.NORMAL)

                if message.startswith("🟢") or message.startswith("🔴"):
                    chat_area.insert(tk.END, message + "\n", "server")

                elif message.startswith(username + ":"):
                    chat_area.insert(tk.END, message + "\n", "self")

                else:
                    chat_area.insert(tk.END, message + "\n", "other")

                chat_area.config(state=tk.DISABLED)
                chat_area.see(tk.END)

        except:
            client.close()
            break


receive_thread = threading.Thread(target=receive)
receive_thread.daemon = True
receive_thread.start()

message_entry.bind("<Return>", lambda event: write())

root.mainloop()
