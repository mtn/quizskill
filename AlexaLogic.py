import random

class Alexa:
	def repromptForTopic(self):
		return question(render_template('no_topic'))

	def sayFailureMessage(self, topic):
		return question(render_template('topic_failure', topic=topic))

	def sayConfirmedTopicMessage(self, topic, term):
		return question(render_template('confirm_topic', 
						topic=topic, 
						term=term))

	def saveAttributeInSession(self, attribute, value):
		session.attributes[attribute] = value

class AlexaLogic:
	def __init__(self, Alexa = None):
		self.Alexa = Alexa

	def study_handler(self, topic):
		if topic == None or topic == "":
			return self.Alexa.repromptForTopic()

		self.Alexa.saveAttributeInSession("topic", topic)

		client_secret = self.getClientID()
		client = self.getQuizletClient()

		query_result = self.queryQuizletClient(client, topic)
		if len(query_result['sets']) == 0:
			return self.Alexa.sayFailureMessage(topic)

		use = False
		while not use:
			choice = random.choice(query_result['sets'])
			user_set = selectQuizletClientSet(client, choice['id'])

			check = min(len(user_set['terms']), 20)
			use = True
			for i in range(0, check):
				if user_set['terms'][i]['definition'] == '':
					use = False
					break

			self.Alexa.saveAttributeInSession("set_id", choice['id'])

		self.Alexa.saveAttributeInSession("last_ind", 0)
		self.Alexa.saveAttributeInSession("last_def", user_set['terms'][0]['definition'])
		return self.Alexa.sayConfirmedTopicMessage(topic, user_set['terms'][0]['term'])


	def getClientID(self):
		return environ.get('CLIENT_ID')

	def getQuizletClient(self):
		return quizlet.QuizletClient(client_id=client_secret)

	def queryQuizletClient(self, client, topic):
		return client.api.search.sets.get(params={ 'q': topic })

	def selectQuizletClientSet(self, client, keyword):
		return client.api.sets.get(choice['id'])