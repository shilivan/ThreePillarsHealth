async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    if (!userInput) return;

    // Display user message
    const messagesDiv = document.getElementById('messages');
    const userMessageDiv = document.createElement('div');
    userMessageDiv.textContent = `You: ${userInput}`;
    messagesDiv.appendChild(userMessageDiv);

    try {
        console.log(`Sending message: ${userInput}`);

        // Fetch the GPT API URL from environment variable
        const response = await fetch('/api-url', {
            method: 'GET'
        });
        const { apiUrl } = await response.json();

        // Send message to the bot
        const botResponse = await fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: userInput })
        });

        if (!botResponse.ok) {
            throw new Error(`HTTP error! status: ${botResponse.status}`);
        }

        const data = await botResponse.json();
        console.log(`Received response: ${data.response}`);

        // Display bot response
        const botMessageDiv = document.createElement('div');
        botMessageDiv.textContent = `TCM Study Buddy: ${data.response}`;
        messagesDiv.appendChild(botMessageDiv);
    } catch (error) {
        console.error('Error during fetch:', error);
        const errorMessageDiv = document.createElement('div');
        errorMessageDiv.textContent = `Error: ${error.message}`;
        messagesDiv.appendChild(errorMessageDiv);
    }

    // Clear input field
    document.getElementById('user-input').value = '';
}
