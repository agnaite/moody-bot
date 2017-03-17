from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(
    'Dude',
    trainer='chatterbot.trainers.ChatterBotCorpusTrainer',
)

chatbot.train("chatterbot.corpus.english")
chatbot.train("chatterbot.corpus.english.greetings")
chatbot.train("chatterbot.corpus.english.conversations")
# chatbot.train("chatterbot.corpus.english.swear_words")
chatbot.train("chatterbot.corpus.english.emotions")

chatbot.set_trainer(ListTrainer)

for i in range(200):
    chatbot.train([
        "What's up dude?",
        "What's up dude",
    ])
