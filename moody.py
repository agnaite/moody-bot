from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
    'Andy',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
)


def train_with_corpus(corpus):
    """Trains using json corpi"""

    chatbot.set_trainer("chatterbot.trainers.ChatterBotCorpusTrainer")
    chatbot.train(corpus)


def train_andy(question, answer):
    """Train the bot with phrase pairs"""

    chatbot.set_trainer(ListTrainer)

    chatbot.train([
        question,
        answer,
    ])
