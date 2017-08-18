from flask_ask import Ask, statement
from flask import Flask, request
from os import environ
import quizlet

app = Flask(__name__)
ask = Ask(app, '/')

# Should be true on production
app.config['ASK_VERIFY_REQUESTS'] = False

@ask.intent("StudyIntent")
def study_handler(topic):
    speech_text = "Let's study %s" % topic
    return statement(speech_text)


if __name__ == '__main__':
    app.run()


    #
    #         client_secret = environ.get('CLIENT_ID')
    #         client = quizlet.QuizletClient(client_id=client_secret)
    #
    #         query_result = client.api.search.sets.get(params={ 'q': query })
    #         print(query_result)
    #
    # return 'Hello, World!'
