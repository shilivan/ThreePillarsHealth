async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (!userInput) return;

    // Display user message
    const messagesDiv = document.getElementById('messages');
    const userMessageDiv = document.createElement('div');
    userMessageDiv.textContent = `You: ${userInput}`;
    messagesDiv.appendChild(userMessageDiv);

    // Send message to backend
    const response = await fetch('https://your-backend-url/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    });

    const data = await response.json();

    // Display GPT response
    const botMessageDiv = document.createElement('div');
    botMessageDiv.textContent = `TCM Study Buddy: ${data.response}`;
    messagesDiv.appendChild(botMessageDiv);

    // Clear input field
    document.getElementById('user-input').value = '';
}
