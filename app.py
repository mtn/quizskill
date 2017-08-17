from flask import Flask, request
from os import environ
import quizlet


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def quizlet_handler():

    if request.method == 'POST':
        raw_data = request.get_json()

        query = raw_data["request"]["intent"]["slots"]["query"]

        client_secret = environ.get('CLIENT_ID')
        client = quizlet.QuizletClient(client_id=client_secret)

        query_result = client.api.search.sets.get(params={ 'q': query })
        print(query_result)

    return 'Hello, World!'

if __name__ == '__main__':
    app.run()
