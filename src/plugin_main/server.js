const WebSocket = require('ws');

const connectedClients = new Set();

const server = new WebSocket.Server({ port: 8080 });

server.on('connection', (websocket) => {
  connectedClients.add(websocket);

  websocket.on('message', (message) => {
    console.log(`Received message from client: ${message}`);
    for (const client of connectedClients) {
      if (client !== websocket) {
        client.send(message);
        // repeat the message
        const data = {
          sender: 'Bot',
          time: 'Now',
          text: message
        };
        client.send(JSON.stringify(data));
      }
    }
  });

  websocket.on('close', () => {
    console.log('Client disconnected');
    connectedClients.delete(websocket);
  });
});