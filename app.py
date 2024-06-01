import openai
import os
import asyncio
from flask import Flask, request, jsonify

app = Flask(__name__)

openai.api_key = os.getenv('THREEPILLARSHEALTH')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=150
    )
    return jsonify({'response': response.choices[0].text.strip()})

async def async_function():
    await asyncio.sleep(1)
    return "Async Response"

@app.route('/async')
def handle_async():
    loop = asyncio.get_event_loop()
    result = loop.run_until_complete(async_function())
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
