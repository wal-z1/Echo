from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from pathlib import Path
# important imports will be useful later

app = FastAPI()

# an object to store currently connected users (since no db)
connected_users = {}

@app.get("/")
async def main():
    html = Path("chat.html").read_text()  # open file in that path and read the text
    # return to the user the page text as an html response
    return HTMLResponse(html)

@app.websocket("/ws/{user}")
async def websocket_endpoint(websocket: WebSocket, user: str): 
      # import the websocket created and the user (from URL path)
      await websocket.accept()  # wait until the browser accepts the websocket request
      connected_users[user] = websocket  # add the user and their websocket to the dict 
      
      try:  # try to keep the connection open
          while True:
               # wait for the client to send data in JSON format
               data = await websocket.receive_json()  
               
               to = data["to"]
               message = data["message"]

               # check if the receiver exists among connected users
               if to in connected_users:
                    # send a JSON object to the receiver's websocket
                    await connected_users[to].send_json({
                        "from": user,     # who sent the message
                        "message": message  # the message itself
                    })
               else:
                    # if receiver not connected, notify the sender
                    await websocket.send_json({"error": f"{to} is not connected"})

      except WebSocketDisconnect:
        # if the user disconnects, remove them from the connected list
        del connected_users[user]
