#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import asyncio
import websockets

connected_clients = set()


async def chat_handler(websocket, path):
    connected_clients.add(websocket)
    try:
        while True:
            message = await websocket.recv()
            print("message====", message, connected_clients)
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
                    # repeat the message
                    data = {
                        'sender': 'Bot',
                        'time': 'Now',
                        'text': message
                    }
                    await client.send(str(data))
    except websockets.ConnectionClosed:
        connected_clients.remove(websocket)


start_server = websockets.serve(chat_handler, "localhost", 8080)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()