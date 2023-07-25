Sure! Here's the code for the file `backend/main.py`:

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/chatbot', methods=['POST'])
def handle_chatbot_request():
    # Get the incoming message from the chatbot
    message = request.json['message']

    # TODO: Implement NLP-based response generation logic here

    # Generate a response based on the message
    response = generate_response(message)

    # Return the response to the chatbot
    return {'response': response}

def generate_response(message):
    # TODO: Implement NLP-based response generation logic here
    return 'This is a sample response.'

if __name__ == '__main__':
    app.run()
```

This code sets up a Flask server that listens for POST requests at the `/chatbot` endpoint. When a request is received, it extracts the incoming message from the chatbot, generates a response using NLP-based logic (which you need to implement), and returns the response to the chatbot.

Please note that the `generate_response` function is a placeholder and needs to be implemented with your NLP-based response generation logic.

Let me know if you need any further assistance!