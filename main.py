from flask import Flask, request
import quizlet
import json


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def quizlet_handler():

    if request.method == 'POST':
        raw_data = request.get_json()

        query = raw_data["request"]["intent"]["slots"]["query"]

        with open("secrets.json","r") as secrets:
            secrets = json.loads(secrets.read())

            client = quizlet.QuizletClient(client_id=secrets['client_id'])

            query_result = client.api.search.sets.get(params={ 'q': query })
            print(query_result)

    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
