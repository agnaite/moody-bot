# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request
from flask_assets import Environment
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


app = Flask(__name__)
assets = Environment(app)

# assets.url = app.static_url_path

chatbot = ChatBot(
    'Dude',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
)

chatbot.train("chatterbot.corpus.english")
chatbot.train("chatterbot.corpus.english.greetings")
chatbot.train("chatterbot.corpus.english.conversations")

chatbot.set_trainer(ListTrainer)

for i in range(200):
    chatbot.train([
        "What's up dude?",
        "What's up dude",
    ])


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
