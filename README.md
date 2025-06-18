🔐 Cipher-Chat

📌 Description

secure-chat is a secure, real-time chat application developed in Python. It leverages socket programming for network communication and utilizes Fernet encryption (AES 128-bit) to provide end-to-end message security between users. The application features a command-line interface (CLI) for ease of use and is suitable for both LAN and Internet-based communication (with appropriate port forwarding).

⚙️ Tech Stack

- Python (socket, threading)
- cryptography (Fernet - AES 128-bit)
- Command-Line Interface (CLI)

🔐 Features

- ✅ End-to-end encrypted messaging  
- ✅ Supports multiple clients  
- ✅ Real-time chat via a central server  
- ✅ Operates on LAN or over the Internet (with port forwarding)

🚀 Getting Started

### 1. Prerequisites
- Python 3.7 or higher must be installed on your system.
- Download it from [python.org](https://www.python.org/).

### 2. Install Dependencies
Install the required Python packages using pip:
```bash
pip install -r requirements.txt

3. Running the Server

Start the chat server:

python server.py

4. Running the Client

Start a chat client:

python client.py

    You can run multiple clients on different terminals or machines to simulate multiple users.

🛡️ Security

    All messages are encrypted using Fernet (AES 128-bit) before transmission.

    Only intended recipients can decrypt and read the messages.

    The server relays encrypted messages and does not have access to plaintext content.

🌐 Network Configuration

    For LAN usage, ensure all clients are on the same network and can access the server's IP and port.

    For Internet usage, configure port forwarding on your router to allow external clients to connect to the server's IP and port (default: 12345).

📡 Friend Network Setup (for others to connect)

To connect to the server from a different machine:

    Get Server IP Address:

        Run ipconfig (Windows) or ifconfig (Linux/macOS) on the machine running the server.

        Note the IPv4 Address, e.g., 192.168.1.12.

    Update Client IP:

        In client.py, change the line:

HOST = '127.0.0.1'

to:

    HOST = '192.168.1.12'  # Replace with the actual server IP

Use the Same Encryption Key:

    All clients must use the same Fernet KEY inside client.py. Generate it once using:

from crypto_utils import generate_key

Paste the key in all client files:

        KEY = b'your_generated_key_here'

    Allow Firewall/Port Access:

        Ensure Python is allowed through the firewall on the server.

        Use port 12345 (or change if needed in server.py and client.py).

📄 License

This project is licensed under the MIT License. See the LICENSE file for details.

📫 Contact

For questions or support, contact me at: your.email@example.com
