# Echo

**Overview**
Echo is a real-time chat app with a FastAPI WebSocket backend and a React + Vite frontend. Users join rooms by URL, and messages broadcast to everyone connected to the same room.

**Architecture**

- **Backend:** FastAPI WebSocket endpoint at `/ws/{room}/{user}`
- **Frontend:** React Router route `/chat/:room/:user` that opens a WebSocket connection

**Backend behavior**

- Tracks active sockets per room in a simple connection manager
- Broadcasts join, message, and leave events to the room
- Removes broken sockets on error to keep rooms clean

**Frontend behavior**

- Reads `room` and `user` from the URL
- Connects to `ws://127.0.0.1:1000/ws/{room}/{user}`
- Renders the live message stream and sends user input

**Run locally**

1. **Backend** (from the repo root)
   - Create and activate a virtual environment
     - Windows PowerShell:
       - `python -m venv .venv`
       - `.\.venv\Scripts\Activate.ps1`
     - Windows Command Prompt:
       - `python -m venv .venv`
       - `.\.venv\Scripts\activate.bat`
     - macOS/Linux:
       - `python3 -m venv .venv`
       - `source .venv/bin/activate`
   - Install dependencies from [requirements.txt](requirements.txt)
     - `pip install -r requirements.txt`
   - Start the server
     - `uvicorn main:app --host 127.0.0.1 --port 1000 --reload`
2. **Frontend** (from [front/echo-front](front/echo-front))
   - Install dependencies: `npm install`
   - Start the dev server: `npm run dev`

**Stop the environment**

- Stop servers with `Ctrl+C` in each terminal
- Deactivate the virtual environment with `deactivate`

**Use the app**

- Open a room in the browser: `http://localhost:5173/chat/general/john`
- Open another tab with a different name to see real-time updates
