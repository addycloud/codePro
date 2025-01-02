import asyncio
import websockets
import json
import logging
from typing import Callable, Optional

# 配置
class WebSocketConfig:
    def __init__(self, uri, heartbeat_interval=10, max_reconnect_attempts=5, reconnect_delay=5):
        self.uri = uri
        self.heartbeat_interval = heartbeat_interval
        self.max_reconnect_attempts = max_reconnect_attempts
        self.reconnect_delay = reconnect_delay

# WebSocket 客户端
class WebSocketClient:
    def __init__(self, config: WebSocketConfig):
        self.config = config
        self.websocket = None
        self.is_connected = False
        self.reconnect_attempts = 0
        self.heartbeat_task = None
        self.message_queue = asyncio.Queue()
        self.logger = logging.getLogger("WebSocketClient")

        # 事件回调
        self.on_connected: Optional[Callable] = None
        self.on_disconnected: Optional[Callable] = None
        self.on_message: Optional[Callable] = None

    async def connect(self):
        """连接到 WebSocket 服务器"""
        while self.reconnect_attempts < self.config.max_reconnect_attempts:
            try:
                self.websocket = await websockets.connect(self.config.uri)
                self.is_connected = True
                self.reconnect_attempts = 0
                self.logger.info(f"Connected to {self.config.uri}")

                # 触发连接成功回调
                if self.on_connected:
                    self.on_connected()

                # 启动心跳任务
                self.heartbeat_task = asyncio.create_task(self.send_heartbeat())

                # 启动消息发送任务
                asyncio.create_task(self.process_message_queue())

                return
            except Exception as e:
                self.reconnect_attempts += 1
                self.logger.error(
                    f"Connection failed (attempt {self.reconnect_attempts}/{self.config.max_reconnect_attempts}): {e}"
                )
                await asyncio.sleep(self.config.reconnect_delay)

        self.logger.error("Max reconnection attempts reached. Giving up.")

    async def send(self, message):
        """将消息放入发送队列"""
        await self.message_queue.put(message)

    async def process_message_queue(self):
        """处理消息队列中的消息"""
        while self.is_connected:
            try:
                message = await self.message_queue.get()
                if self.websocket:
                    await self.websocket.send(message)
                    self.logger.info(f"Sent: {message}")
            except Exception as e:
                self.logger.error(f"Failed to send message: {e}")
                await self.handle_disconnection()

    async def receive(self):
        """接收来自 WebSocket 服务器的消息"""
        while self.is_connected:
            try:
                if self.websocket:
                    response = await self.websocket.recv()
                    self.logger.info(f"Received: {response}")

                    # 触发消息接收回调
                    if self.on_message:
                        self.on_message(response)
            except Exception as e:
                self.logger.error(f"Failed to receive message: {e}")
                await self.handle_disconnection()

    async def send_heartbeat(self):
        """发送心跳消息"""
        while self.is_connected:
            try:
                heartbeat_message = json.dumps({"type": "heartbeat"})
                await self.send(heartbeat_message)
                await asyncio.sleep(self.config.heartbeat_interval)
            except Exception as e:
                self.logger.error(f"Heartbeat failed: {e}")
                await self.handle_disconnection()

    async def handle_disconnection(self):
        """处理连接断开"""
        self.is_connected = False
        if self.heartbeat_task:
            self.heartbeat_task.cancel()
        await self.close()

        # 触发断开连接回调
        if self.on_disconnected:
            self.on_disconnected()

        # 尝试重新连接
        await self.connect()

    async def close(self):
        """关闭 WebSocket 连接"""
        if self.websocket:
            await self.websocket.close()
            self.websocket = None
            self.logger.info("Connection closed")

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

# 使用示例
async def main():
    # 配置日志
    logging.basicConfig(level=logging.INFO)

    # WebSocket 配置
    config = WebSocketConfig(uri="ws://example.com/ws", heartbeat_interval=10, max_reconnect_attempts=5)

    # 创建客户端
    async with WebSocketClient(config) as client:
        # 设置事件回调
        client.on_connected = lambda: logging.info("Connected to server!")
        client.on_disconnected = lambda: logging.info("Disconnected from server!")
        client.on_message = lambda msg: logging.info(f"Received message: {msg}")

        # 发送消息
        await client.send(json.dumps({"type": "greeting", "content": "Hello, WebSocket!"}))

        # 保持运行
        while True:
            await asyncio.sleep(1)

# 运行主函数
asyncio.get_event_loop().run_until_complete(main())