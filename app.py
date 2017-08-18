from flask_ask import Ask, statement
from flask import Flask, request
from os import environ
import quizlet

app = Flask(__name__)
ask = Ask(app, '/')


if __name__ == '__main__':
    app.run()

# @ask.intent('StudyIntent')
# def hello():
    # return statement("StudyIntent")

# @ask.intent("StudyIntent")
# def study_handler(topic):
#     # speech_text = "Let's study %s" % topic
#     speech_text = "This was invoked"
#     return statement(speech_text)
        #
    #     if raw_data["request"]["intent"]["name"] == "StudyIntent":
    #         query = raw_data["request"]["intent"]["slots"]["topic"]["value"]
    #
    #         client_secret = environ.get('CLIENT_ID')
    #         client = quizlet.QuizletClient(client_id=client_secret)
    #
    #         query_result = client.api.search.sets.get(params={ 'q': query })
    #         print(query_result)
    #
    # return 'Hello, World!'
