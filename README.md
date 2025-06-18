# 🔐 CipherChat

## 📌 Description

**CipherChat** is a cutting-edge, secure, real-time chat application developed in Python. It leverages socket programming for seamless network communication and utilizes **Fernet encryption (AES 128-bit)** to ensure end-to-end message security between users. Designed for simplicity and reliability, CipherChat supports both **LAN** and **Internet-based communication** with port forwarding, making it ideal for private and secure conversations.

---

## ⚙️ Tech Stack

- **Python** (`socket`, `threading`)
- **cryptography** (Fernet - AES 128-bit)
- **Graphical User Interface (GUI)** or **Command-Line Interface (CLI)**

---

## 🔐 Features

- ✅ **End-to-End Encrypted Messaging**: Ensures complete privacy for all communications.  
- ✅ **Multi-Client Support**: Connect multiple users to the same server.  
- ✅ **Real-Time Communication**: Instant messaging via a centralized server.  
- ✅ **Cross-Network Compatibility**: Operates on LAN or over the Internet (with port forwarding).  
- ✅ **Timestamped Messages**: Displays sender name and time for clarity.  

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.7 or higher must be installed on your system.  
  Download it from [python.org](https://www.python.org/).

### 2. Install Dependencies
Install the required Python packages using pip:
```bash
pip install -r requirements.txt
```

### 3. Running the Server
Start the chat server:
```bash
python server.py
```

### 4. Running the Client
Start a chat client:
```bash
python client_gui.py
```
You can run multiple clients on different terminals or machines to simulate multiple users.

---

## 🛡️ Security

- **End-to-End Encryption**: All messages are encrypted using **Fernet (AES-128)** before transmission.  
- **Privacy by Design**: Only intended recipients can decrypt and read the messages.  
- **Server Transparency**: The server relays encrypted messages and does not have access to plaintext content.  

---

## 🌐 Network Configuration

### For LAN Usage:
- Ensure all clients are on the same network and can access the server's IP and port.

### For Internet Usage:
- Configure **port forwarding** on your router to allow external clients to connect to the server's IP and port (default: `12345`).

---

## 📡 Friend Network Setup (for Others to Connect)

### 1. Get Server IP Address:
- On the machine running the server, run:
  - **Windows**: `ipconfig`
  - **Linux/macOS**: `ifconfig`
- Note the **IPv4 Address** (e.g., `192.168.1.12`).

### 2. Update Client IP:
- In `client_gui.py`, change the line:
  ```python
  HOST = '127.0.0.1'
  ```
  to:
  ```python
  HOST = '192.168.1.12'  # Replace with the actual server IP
  ```

### 3. Use the Same Encryption Key:
- All clients must use the same **Fernet KEY** inside `client_gui.py`. Generate it once using:
  ```python
  from crypto_utils import generate_key
  ```
- Paste the key in all client files:
  ```python
  KEY = b'your_generated_key_here'
  ```

### 4. Allow Firewall/Port Access:
- Ensure Python is allowed through the firewall on the server.
- Use port `12345` (or change it in `server.py` and `client_gui.py`).

---

## 📄 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 📫 Contact

For questions or support, contact me at: **your.email@example.com**
