// 获取页面元素
const conversationElement = document.getElementById('conversation');
const userInputElement = document.getElementById('userInput');
const sendButtonElement = document.getElementById('sendButton');

// 定义对话数组
const conversation = [];

// 发送消息
function sendMessage() {
  const message = userInputElement.value.trim();
  if (message !== '') {
    // 添加用户消息到对话数组
    conversation.push({ role: 'user', content: message });
    updateConversation();

    // 调用 tokenizer 函数
    fetch('/tokenizer', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ messages: conversation })
    })
      .then(response => response.json())
      .then(data => {
        // 处理返回的结果
        conversation.push({ role: 'bot', content: data.result });
        updateConversation();
      })
      .catch(error => {
        console.error('Error:', error);
      });

    // 清空输入框
    userInputElement.value = '';
  }
}

// 更新对话显示
function updateConversation() {
  conversationElement.innerHTML = '';
  conversation.forEach(message => {
    const messageElement = document.createElement('div');
    messageElement.classList.add(message.role);
    messageElement.textContent = message.content;
    conversationElement.appendChild(messageElement);
  });
}

// 监听发送按钮点击事件
sendButtonElement.addEventListener('click', sendMessage);

// 监听输入框回车键按下事件
userInputElement.addEventListener('keydown', event => {
  if (event.key === 'Enter') {
    sendMessage();
  }
});