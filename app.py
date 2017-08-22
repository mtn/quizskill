from flask_ask import Ask, statement
from flask import Flask, request
from os import environ
import quizlet
import random

app = Flask(__name__)
ask = Ask(app, '/')

# Should be true on production
app.config['ASK_VERIFY_REQUESTS'] = False

@ask.launch
def launch_handler():
    return question('Welcome to Study Helper')

@ask.on_session_started
def new_session():
    log.info('New session started')

@ask.intent("StudyIntent")
def study_handler(topic):
    client_secret = environ.get('CLIENT_ID')
    client = quizlet.QuizletClient(client_id=client_secret)

    query_result = client.api.search.sets.get(params={ 'q': query })

    return question(render_template())

@ask.session_ended
def session_end_handler():
    log.info('Session ended')
    return "", 200


if __name__ == '__main__':
    app.run(debug=True)

