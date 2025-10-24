from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List, Dict  # for casting


app = FastAPI()

@app.get("/")
def rootacc():
    return{"message":"HelloThere"}
#just a normal hellow world

#we need to track the connections in order to do so we use a class

class ConnectionManager():
    def __init__(self):
    #Store active connections. The structure is:
    # { "room_name": [websocket1, websocket2, ...] }        init to an empty dict

        self.Rooms: Dict[str,list[WebSocket]] = {}   
    async def connect(self,socket : WebSocket, room:str):
        await socket.accept()  ##let browser accept the new websocket connection 

        if room not in self.Rooms:
            self.Rooms[room]= [] 
            #access int the rooms this room field and make a list for the websockets
            self.Rooms[room].append(socket)

    async def dissconnect(self,socket:WebSocket, room:str):
        self.Rooms[room].remove(socket)
    async def send(self, message:str,room:str):
        for ppl in self.Rooms[room]:
            await ppl.send_text(message)

#define 3    async function eah for the three elementary actions

ConnectionNum1= ConnectionManager() ## create one connection manager
