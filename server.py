# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request
from flask_assets import Environment
from moody import chatbot
import os


app = Flask(__name__)
assets = Environment(app)


@app.route("/")
def home():

    question = request.args.get('question')

    if question:
        response = chatbot.get_response(question)
        return jsonify(response.text)
    else:
        return render_template('base.html')


if __name__ == "__main__":

    PORT = int(os.environ.get("PORT", 5000))
    DEBUG = "NO_DEBUG" not in os.environ

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
