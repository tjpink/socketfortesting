# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 13:01:50 2021

@author: tjpin
"""

#!/usr/bin/env python
import asyncio
import websockets

msg_reply = "(Message received by the server.)"
msg_received=""
localhostIP =  "169.254.4.112"
print("Localhost IP address: " + localhostIP)

async def server(websocket, path):
    async for message in websocket:
        msg_received = message
        print(message)
        await websocket.send(msg_reply)

start_server = websockets.serve(server, localhostIP, 5000)



asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

while True:
    if msg_received == "It's me":
        print("okay")
