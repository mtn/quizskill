from flask_ask import Ask, statement
from flask import Flask, request
from os import environ
import quizlet

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
    speech_text = "Alright, let's study %s" % topic

    client_secret = environ.get('CLIENT_ID')
    client = quizlet.QuizletClient(client_id=client_secret)

    query_result = client.api.search.sets.get(params={ 'q': query })

    return statement(speech_text)

@ask.session_ended
def session_end_handler():
    return "", 200


if __name__ == '__main__':
    app.run(debug=True)

    #         print(query_result)
