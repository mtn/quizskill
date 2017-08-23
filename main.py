from flask_ask import Ask, statement, question, session
from flask import Flask, request, render_template
from os import environ
import quizlet
import random

app = Flask(__name__)
ask = Ask(app, '/')

# Should be true on production
app.config['ASK_VERIFY_REQUESTS'] = False

template_correct = [ "term1_c", "term2_c", "term3_c" ]
template_incorrect = [ "term1_i", "term2_i", "term3_i" ]

@ask.launch
def launch_handler():
    return question("Welcome to study helper. What do you want help studying?")

@ask.intent("StudyIntent")
def study_handler(topic):
    session.attributes['topic'] = topic

    client_secret = environ.get('CLIENT_ID')
    client = quizlet.QuizletClient(client_id=client_secret)

    query_result = client.api.search.sets.get(params={ 'q': topic })

    use = False
    while not use:
        ind = random.randint(0,len(query_result['sets']))
        session.attributes['set_id'] = query_result['sets'][ind]['id']
        user_set = client.api.sets.get(session.attributes['set_id'])

        check = min(len(user_set['terms']),20)
        use = True
        for i in range(0,check):
            if user_set['terms'][i]['definition'] == '':
                use = False
                break

    session.attributes['last_ind'] = 0
    session.attributes['last_def'] = user_set['terms'][0]['definition']
    return question(render_template('confirm_topic',
                    topic=topic,
                    term=user_set['terms'][0]['term']))

@ask.intent("GetTerm")
def term_handler(response=None):
    if 'topic' not in session.attributes:
        return question("Sorry, what do you want me to help you study?")

    topic = session.attributes['topic']
    query_result = client.api.search.sets.get(params={ 'q': topic })

    if 'set_id' not in session.attributes:
        use = False
        while not use:
            ind = random.randint(0,len(query_result['sets']))
            session.attributes['set_id'] = query_result['sets'][ind]['id']

            check = min(len(user_set['terms']),20)
            use = True
            for i in range(0,check):
                if user_set['terms'][i]['definition'] == '':
                    use = False
                    break

    if 'last_def' in session.attributes:
        return response == session.attributes['last_def']
    return "hi"

    # session.attributes['last_def'] = user_set['terms'][0]['definition']
    # if 'last_ind' in session_attributes:
    #     session_attributes['last_ind'] = session_attributes['last_ind'] + 1
    # else:
    #     session_attributes['last_ind'] = 0

    # template_ind = random.randint(0,3)








if __name__ == '__main__':
    app.run()

