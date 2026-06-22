# Task 5 - Chat Application

A real-time GUI chat application using Python sockets and Tkinter.

## Features
- Real-time messaging between multiple users
- Username support
- Color-coded messages (you vs others vs server)
- Emoji bar
- Join/leave notifications

## Installation

```bash
# No extra installs needed — uses only Python built-ins
```

## How to Run

### Step 1 — Start the Server (in one terminal)
```bash
python server.py
```

### Step 2 — Start one or more Clients (in separate terminals)
```bash
python client.py
```

> Open multiple client windows to simulate a group chat!

## How it Works
- `server.py` handles all connections and broadcasts messages to every connected client
- `client.py` provides the GUI and connects to the server

## Author
Jeevan Joyit — Oasis Infobyte Internship 2026
