from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Replace 'your-openai-api-key' with your actual OpenAI API key
openai.api_key = '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'

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
