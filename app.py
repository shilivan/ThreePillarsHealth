import openai
import os
import asyncio
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(name)s %(message)s')
logger = logging.getLogger(__name__)

# Get OpenAI API key from environment variable
openai.api_key = os.getenv('THREEPILLARSHEALTH')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message')
    logger.debug(f'Received message: {user_message}')
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=150
        )
        result = response.choices[0].text.strip()
        logger.debug(f'GPT response: {result}')
        return jsonify({'response': result})
    except Exception as e:
        logger.error(f'Error connecting to GPT: {e}')
        return jsonify({'error': str(e)}), 500

async def async_function():
    await asyncio.sleep(1)
    return "Async Response"

@app.route('/async')
def handle_async():
    loop = asyncio.get_event_loop()
    try:
        result = loop.run_until_complete(async_function())
        logger.debug(f'Async function result: {result}')
        return result
    except Exception as e:
        logger.error(f'Error in async function: {e}')
        return str(e), 500

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
        logger.info("Flask app started successfully.")
    except Exception as e:
        logger.error(f'Error starting Flask app: {e}')
