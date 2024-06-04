import openai
import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Load the API key and URL from environment variables
openai.api_key = os.getenv('OPENAI_API_KEY')
gpt_api_url = os.getenv('GPT_API_URL')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.json
        user_message = data.get('message')
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=150
        )
        return jsonify({'response': response.choices[0].text.strip()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api-url', methods=['GET'])
def get_api_url():
    return jsonify({'apiUrl': gpt_api_url})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
