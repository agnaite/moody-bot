# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request
from chatterbot import ChatBot

app = Flask(__name__)

chatbot = ChatBot(
    'Dude',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer'
)

chatbot.train("chatterbot.corpus.english")
chatbot.train("chatterbot.corpus.english.greetings")
chatbot.train("chatterbot.corpus.english.conversations")


@app.route("/")
def home():

    question = request.args.get('question')

    if question:
        response = chatbot.get_response(question)
        return jsonify(response.text)
    else:
        return render_template('base.html')


if __name__ == "__main__":
    app.run(debug=True)
