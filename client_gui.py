import socket
import threading
from crypto_utils import encrypt_message, decrypt_message
from datetime import datetime
import tkinter as tk
from tkinter import simpledialog, scrolledtext, messagebox

KEY = b'8oq1_zjo5aAG69nwamvCzN70YoTF9NewKdwHqsflZ7E='
HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((HOST, PORT))
except Exception as e:
    messagebox.showerror("Connection Error", f"Could not connect to server: {e}")
    exit()

# --- GUI Setup ---
root = tk.Tk()
root.title("CipherChat")
root.configure(bg="#003300")

# Prompt for username before showing chat window
def prompt_username():
    prompt = tk.Toplevel(root)
    prompt.title("Enter Name")
    prompt.geometry("300x120")
    prompt.configure(bg="#003300")
    prompt.grab_set()
    prompt.resizable(False, False)

    label = tk.Label(prompt, text="Enter your name:", fg="#00FF00", bg="#003300", font=("Consolas", 12))
    label.pack(pady=(20, 5))

    name_var = tk.StringVar()

    entry = tk.Entry(prompt, textvariable=name_var, fg="#00FF00", bg="#001a00", insertbackground="#00FF00", font=("Consolas", 12))
    entry.pack(pady=(0, 10))
    entry.focus()

    def submit():
        if name_var.get().strip():
            prompt.destroy()
        else:
            messagebox.showwarning("Input Error", "Name cannot be empty.")

    entry.bind("<Return>", lambda event: submit())
    btn = tk.Button(prompt, text="OK", command=submit, fg="#00FF00", bg="#002200", font=("Consolas", 10, "bold"))
    btn.pack()

    root.wait_window(prompt)
    return name_var.get().strip()

username = prompt_username()
if not username:
    username = "Anonymous"

# Date label
date_label = tk.Label(root, text=datetime.now().strftime('%A, %d %B %Y'), fg="#00FF00", bg="#003300", font=("Consolas", 10, "bold"))
date_label.pack(pady=(10,0))

# Chat area
chat_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', fg="#00FF00", bg="#002200", font=("Consolas", 12))
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Message entry
msg_entry = tk.Entry(root, fg="#00FF00", bg="#001a00", insertbackground="#00FF00", font=("Consolas", 12))
msg_entry.pack(padx=10, pady=(0,10), fill=tk.X)
msg_entry.focus()

def receive():
    while True:
        try:
            encrypted_msg = client.recv(1024)
            msg = decrypt_message(encrypted_msg, KEY)
            # Parse message to extract sender
            try:
                time_part, rest = msg.split('] ', 1)
                sender, message = rest.split(': ', 1)
                if sender == username:
                    display = f"{time_part[1:]} You: {message}"
                else:
                    display = f"{time_part[1:]} {sender}: {message}"
            except Exception:
                display = msg
            chat_area.config(state='normal')
            chat_area.insert(tk.END, display + "\n")
            chat_area.config(state='disabled')
            chat_area.see(tk.END)
        except:
            break

def send(event=None):
    msg = msg_entry.get()
    if msg.strip() == "":
        return
    now = datetime.now().strftime("%H:%M:%S")
    full_msg = f"[{now}] {username}: {msg}"
    encrypted_msg = encrypt_message(full_msg, KEY)
    client.send(encrypted_msg)
    # Show your own message as "You: ..."
    chat_area.config(state='normal')
    chat_area.insert(tk.END, f"{now} You: {msg}\n")
    chat_area.config(state='disabled')
    chat_area.see(tk.END)
    msg_entry.delete(0, tk.END)

msg_entry.bind("<Return>", send)

# Start receiving thread
recv_thread = threading.Thread(target=receive, daemon=True)
recv_thread.start()

root.mainloop()