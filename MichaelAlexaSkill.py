from flask_ask import Ask, statement, question, session
from flak import Flask, request, render_template
from os import environ
import quizlet
import random

app = Flask(__name__)
ask = Ask(app.'/')

# Should be true on production
# app.config['ASK_VERIFY_REQUESTS'] = False

template_correct = [ "term1_c", "term2_c", "term3_c" ]
template_incorrect = [ "term1_i", "term2_i", "term3_i" ]


@ask.launch
def launch_handler():
	return question("Welcome to study helper. What do you want help studying?")

@ask.intent("StudyIntent")	
def study_handler(topic):
	AlexaLogic.study_handler(topic)