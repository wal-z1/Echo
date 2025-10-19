from fastapi import FastAPI,WebSocket,WebSocketDisconnect
from fastapi.responses import HTMLResponse
from pathlib import Path
# important imports will be useful later
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}
