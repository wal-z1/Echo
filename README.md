# Echo

simple real-time chat app built with a FastAPI backend and a React frontend.

**Backend:** FastAPI + WebSockets .............. **Frontend:** React + React Router
### HOW Backend

The FastAPI server manages live chat connections with a lightweight `ConnectionManager` class:

* Keeps track of users in each chat room
* When someone connects to `/ws/{room}/{user}`, they’re added to that room
* Messages are instantly broadcast to everyone in the same room
* Join and leave notifications are sent automatically

### HOW Frontend

React Router handles navigation and passes the room and username to the chat page:

* URL format: `/chat/:room/:user`
* The Chatroom component connects to the WebSocket and manages messages in real time

## Usage

Go to `/chat/{roomName}/{username}` to join a room.
You can open multiple tabs with different usernames to test it out.

Example:
`http://localhost:3000/chat/general/john`


