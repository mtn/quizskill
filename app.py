from flask import Flask, request
from os import environ
from alexa import Alexa
import quizlet

alexa = Alexa("Quizlet")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main_handler():


    if request.method == 'POST':
        raw_data = request.get_json()

        return alexa.route(raw_data)

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
    return 'Hello, World!'

@alexa.intent("StudyIntent", mapping={"topic": "topic"})
def study_handler(session, topic):
    return alexa.response.statement(str(topic))



if __name__ == '__main__':
    app.run()