# 🔐 secure-chat

## 📌 Description

**secure-chat** is a secure, real-time chat application developed in Python. It leverages socket programming for network communication and utilizes Fernet encryption (AES 128-bit) to provide end-to-end message security between users. The application features a command-line interface (CLI) for ease of use and is suitable for both LAN and Internet-based communication (with appropriate port forwarding).

---

## ⚙️ Tech Stack

- Python (`socket`, `threading`)
- `cryptography` (Fernet - AES 128-bit)
- Command-Line Interface (CLI)

---

## 🔐 Features

- ✅ End-to-end encrypted messaging
- ✅ Supports multiple clients
- ✅ Real-time chat via a central server
- ✅ Operates on LAN or over the Internet (with port forwarding)

---

## 🚀 Getting Started

### 1. Prerequisites

- Python 3.7 or higher must be installed on your system.  
  You can download Python from [python.org](https://www.python.org/downloads/).

### 2. Install Dependencies

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

### 3. Running the Server

Start the chat server by executing:

```bash
python server.py
```

### 4. Running the Client

Start a chat client by executing:

```bash
python client.py
```

You can run multiple clients on different terminals or machines to simulate multiple users.

---

## 🛡️ Security

- All messages are encrypted using Fernet (AES 128-bit) before transmission.
- Only intended recipients can decrypt and read the messages.
- The server relays encrypted messages and does not have access to plaintext content.

---

## 🌐 Network Configuration

- For LAN usage, ensure all clients are on the same network and can reach the server's IP and port.
- For Internet usage, configure port forwarding on your router to allow external clients to connect to the server.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

---

## 📫 Contact

For questions or support, please open an