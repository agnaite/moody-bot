from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
    'Andy',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
)

chatbot.train("chatterbot.corpus.english")
chatbot.train("chatterbot.corpus.english.greetings")
chatbot.train("chatterbot.corpus.english.conversations")
# chatbot.train("chatterbot.corpus.english.swear_words")
chatbot.train("chatterbot.corpus.english.emotions")

chatbot.set_trainer(ListTrainer)


def train_andy(question, answer):
    """Train the bot with phrase pairs"""

    chatbot.train([
        question,
        answer,
    ])
