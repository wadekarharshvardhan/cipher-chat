import socket
import threading
from crypto_utils import encrypt_message, decrypt_message
from colorama import init, Fore, Style
from datetime import datetime

init(autoreset=True)

KEY = b'8oq1_zjo5aAG69nwamvCzN70YoTF9NewKdwHqsflZ7E='

HOST = '127.0.0.1'
PORT = 12345

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Get user name
username = input(Fore.GREEN + Style.BRIGHT + "Enter your name: ")

def receive():
    while True:
        try:
            encrypted_msg = client.recv(1024)
            msg = decrypt_message(encrypted_msg, KEY)
            print(Fore.GREEN + msg)
        except:
            print(Fore.RED + "Disconnected from server.")
            break

def send():
    while True:
        msg = input(Fore.GREEN + Style.BRIGHT + "You: ")
        now = datetime.now().strftime("%H:%M:%S")
        full_msg = f"[{now}] {username}: {msg}"
        encrypted_msg = encrypt_message(full_msg, KEY)
        client.send(encrypted_msg)

# Remove the ASCII banner, just show app name and date
print(Fore.GREEN + Style.BRIGHT + "========== CipherChat ==========")
print(Fore.GREEN + datetime.now().strftime('%A, %d %B %Y'))
print(Fore.GREEN + "Connected to the chat server. Type your message and press Enter.")

recv_thread = threading.Thread(target=receive)
recv_thread.start()

send_thread = threading.Thread(target=send)
send_thread.start()
