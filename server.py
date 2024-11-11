from flask import Flask, jsonify, request
from markupsafe import escape
from stateful_bot import ask

app = Flask(__name__)

@app.route('/')
def main():
    return '<h1>Hello, World!</h1>\n<h2>Hello, World!</h2>\n<h3>Hello, World!</h3>'

@app.route('/chat/', methods=['POST'])
def chat():
    question = request.json.get('question')
    answer = ask(question)

    return answer
    # return jsonify({"answer": answer}), 201
