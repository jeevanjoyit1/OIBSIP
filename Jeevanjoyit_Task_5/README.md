# 💬 Real-Time Chat Application

A professional real-time chat application built using **Python**, **Socket Programming**, and **Tkinter GUI**. This project enables multiple users to communicate over a local network through an intuitive graphical interface featuring username support, color-coded messages, emoji integration, and real-time join/leave notifications.

---

## 📌 Project Overview

This application follows a **Client-Server Architecture**:

- **Server** manages all incoming client connections.
- **Clients** connect to the server and exchange messages in real time.
- Supports multiple users simultaneously.
- Provides a clean and user-friendly graphical interface.

---

## ✨ Features

✅ Real-Time Messaging

✅ Multi-User Chat Support

✅ Username Authentication

✅ Color-Coded Messages

✅ Emoji Bar Integration

✅ Join/Leave Notifications

✅ Graphical User Interface (Tkinter)

✅ Lightweight and Fast

✅ Uses Python Built-in Libraries Only

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Core Programming Language |
| Socket | Network Communication |
| Threading | Concurrent Client Handling |
| Tkinter | GUI Development |

---

## 📂 Project Structure

```text
ChatApplication/
│
├── server.py
├── client.py
├── requirements.txt
└── README.md
```

---

## ⚙️ System Architecture

```text
           ┌─────────────┐
           │   Server    │
           └──────┬──────┘
                  │
      ┌───────────┼───────────┐
      │           │           │
      ▼           ▼           ▼
 ┌────────┐ ┌────────┐ ┌────────┐
 │Client 1│ │Client 2│ │Client N│
 └────────┘ └────────┘ └────────┘
```

The server broadcasts messages received from one client to all connected clients.

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/chat-application.git
```

```bash
cd chat-application
```

---

## 📋 Requirements

This project uses only Python built-in modules.

### Python Version

```text
Python 3.8 or Higher
```

### Built-in Libraries Used

```python
socket
threading
tkinter
```

No additional package installation is required.

---

## ▶️ Running the Application

### Step 1: Start the Server

Open a terminal and run:

```bash
python server.py
```

Expected Output:

```text
Server is running...
```

---

### Step 2: Start the Client

Open another terminal and run:

```bash
python client.py
```

Enter a username when prompted.

---

### Step 3: Open Multiple Clients

Run additional instances of:

```bash
python client.py
```

Each window represents a different user in the chat room.

---

## 📖 How It Works

### Server

- Creates a socket and listens for incoming connections.
- Accepts client connections.
- Receives usernames.
- Broadcasts messages to all connected clients.
- Notifies users when someone joins or leaves.

### Client

- Connects to the server.
- Provides a GUI for sending and receiving messages.
- Displays messages with different colors.
- Supports emoji insertion.
- Shows join and leave notifications.

---

## 🎨 User Interface Features

### Chat Window

- Scrollable chat history
- Message input field
- Send button
- Emoji toolbar

### Message Colors

| Message Type | Color |
|-------------|--------|
| Your Messages | Blue |
| Other Users | Green |
| Server Notifications | Red |

---

## 🔒 Future Enhancements

- Private Messaging
- File Sharing
- Voice Chat
- Dark Mode
- Message Encryption
- Online User List
- Chat History Storage
- Group Chat Rooms

---

## 🐞 Common Issues

### Port Already In Use

Error:

```text
WinError 10048
```

Solution:

Change the port number in both:

```python
PORT = 60000
```

or terminate the process using the existing port.

---

### Connection Refused

Error:

```text
ConnectionRefusedError
```

Solution:

Make sure the server is running before starting any client.

---

## 📸 Screenshots

### Server Console

```text
Server is running...
User1 connected
User2 connected
```

### Client Window

```text
+-----------------------------------+
| User1: Hello                      |
| User2: Hi there!                  |
| User3 joined the chat             |
+-----------------------------------+
```

---

## 🎯 Learning Outcomes

Through this project, you will learn:

- Socket Programming
- Client-Server Architecture
- Multi-threading in Python
- GUI Development using Tkinter
- Real-Time Network Communication
- Event-Driven Programming

---

## 👨‍💻 Author

**Jeevan Joyit**

Cyber Security Engineer | Python Developer

Oasis Infobyte Internship Project – 2026

---

## 📜 License

This project is developed for educational and internship purposes.

Feel free to use and modify it for learning and personal projects.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub and sharing it with others.

Happy Coding! 🚀
- `client.py` provides the GUI and connects to the server

## Author
Jeevan Joyit — Oasis Infobyte Internship 2026
