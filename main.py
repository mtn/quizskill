from flask_ask import Ask, statement, question, session
from flask import Flask, request, render_template
from os import environ
import quizlet
import random

app = Flask(__name__)
ask = Ask(app, '/')

# Should be true on production
app.config['ASK_VERIFY_REQUESTS'] = False

@ask.launch
def launch_handler():
    return question("Welcome to study helper. What do you want help studying?")

@ask.intent("StudyIntent")
def study_handler(topic):
    session.attributes['topic'] = topic

    client_secret = environ.get('CLIENT_ID')
    client = quizlet.QuizletClient(client_id=client_secret)

    query_result = client.api.search.sets.get(params={ 'q': topic })

    while True:
        ind = random.randint(0,len(query_result['sets']))
        session.attributes['set_id'] = query_result['sets'][ind]['id']
        user_set = client.api.sets.get(session.attributes['set_id'])

        if not user_set['terms'][0]['definition'] == '':
            break

    session.attributes['last_ind'] = 0
    return question(render_template('confirm_topic',
                    topic=topic,
                    term=user_set['terms'][0]['term']))

@ask.intent("GetTerm")
def term_handler():
    if 'topic' not in session.attributes:
        return question("Sorry, what do you want me to help you study?")

    topic = session.attributes['topic']

    if 'id' not in session.attributes:
        query_result = client.api.search.sets.get(params={ 'q': topic })
        ind = random.randint(0,len(query_result['sets']))
        session.attributes['id'] = query_result['sets'][ind]['id']




if __name__ == '__main__':
    app.run()


    #         print(query_result)
    #
    # return 'Hello, World!'
