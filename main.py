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
    async def sendbrodcast(self, message:str,room:str):
        for ppl in self.Rooms[room]:
            await ppl.send_text(message)

#define 3    async function eah for the three elementary actions

ConnectionNum1= ConnectionManager() ## create one connection manager


#define the websocket by user logic

@app.websocket("/ws/{room}/{user}")
async def websocketendpoint(socket:WebSocket,room:str,user:str):
    await ConnectionNum1.connect(socket,room) ##adds to the room
    await ConnectionNum1.sendbrodcast(f'USER {user} has connected to {room}',room) 
    #broadcasts to all users same info
    try: 
        while True:
            #takes any data sent by any user in tthe room and pass it as a broadcast
            data = await socket.receive_text()
            await ConnectionNum1.sendbrodcast(data,room)
    except WebSocketDisconnect:
        await ConnectionNum1.dissconnect(socket,room)
        await  ConnectionNum1.sendbrodcast(f"Client {user} has dissconnected from room {room}",room)
