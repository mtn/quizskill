from flask_ask import Ask, statement, question, session
from flask import Flask, request, render_template
from os import environ
import quizlet

app = Flask(__name__)
ask = Ask(app, '/')

# Should be true on production
app.config['ASK_VERIFY_REQUESTS'] = False
client_secret = environ.get('CLIENT_ID')
client = quizlet.QuizletClient(client_id=client_secret)

@ask.launch
def launch_handler():
    return question("Welcome to study helper. What do you want help studying?")

@ask.intent("StudyIntent")
def study_handler(topic):
    session.attributes['topic'] = topic
    return question(render_template('confirm_topic',topic=topic))

@ask.intent("GetTerm")
def term_handler():
    query = session.attributes['topic']
    query_result = client.api.search.sets.get(params={ 'q': query })
    return(query_result)




if __name__ == '__main__':
    app.run()


    #         print(query_result)
    #
    # return 'Hello, World!'
