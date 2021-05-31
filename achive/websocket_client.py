# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import asyncio
import websockets

async def message():
    async with websockets.connect("ws://169.254.4.112:5000") as socket:
        msg = input("What do yo want to sent: ")
        await socket.send(msg)
        print(await socket.recv())

asyncio.get_event_loop().run_until_complete(message())
