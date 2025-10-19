from fastapi import FastAPI,WebSocket,WebSocketDisconnect
from fastapi.responses import HTMLResponse
from pathlib import Path
# important imports will be useful later
app = FastAPI()

#an object to store currently connected users (since no db)

connected_users = {}

@app.get("/")
async def main():
    html = Path("chat.html").read_text() # open file in that path  , and read the text
    #return to the user the page text as an html response
    return HTMLResponse(html)

@app.websocket("/ws/{user}")
async def websocket_endpoint(websocket: WebSocket, username: str): 
      #import the websocket created and the user
      await websocket.accept() # wait until the browser accepts the websocket req