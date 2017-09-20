import unittest
from AlexaLogic import *

class MichaelAlexaSkillTest(unittest.TestCase):

	def setUp(self):
		self.alexa = AlexaMock()
		self.alexaLogic = TestableAlexaLogic(self.alexa)

	def test_WhenTopicIsEmpty_ShouldRepromptForTopic(self):
		self.alexa.init()
		self.alexaLogic.study_handler("")
		self.assertTrue(self.alexa.spies["repromptForTopic"])

		self.alexa.init()
		self.alexaLogic.study_handler(None)
		self.assertTrue(self.alexa.spies["repromptForTopic"])

	def test_WhenQuizletHasNoResultsForTopic_ShouldSayFailureMessage(self):
		self.alexa.init()
		self.alexaLogic.study_handler("no_results")
		self.assertTrue(self.alexa.spies["sayFailureMessage"])

	def test_WhenQuizletHasNoResults

class TestableAlexaLogic(AlexaLogic):
	def getClientID(self):
		return "TestID"

	def getQuizletClient(self):
		return QuizletClientMock()

	def queryQuizletClient(self, client, topic):
		return client.query(topic)

	def selectQuizletClientSet(self, client, keyword):
		return client.select(keyword)


class QuizletClientMock:
	def __init__(self):
		self.spies = {}

	def query(self, topic):
		self.spies['query'] = topic

		if topic == "no_results":
			return {
				"sets": []
			}
		else:
			return {
				"sets": [{
					"id": 10
				}, {
					"id": 20
				}, {
					"id": 100
				}]
			}
	def select(self, keyword):
		self.spies['select'] = keyword

		return {
			"terms": [{
				"definition": "java",
				'term': "jvm"
			}, {
				"definition": "python",
				"term": "pip"
			}]
		}

class AlexaMock:
	def __init__(self):
		self.session = {}

		self.init()

	def init(self):
		self.spies = {
			"repromptForTopic": False,
			"sayFailureMessage": False
		}

	def repromptForTopic(self):
		self.spies["repromptForTopic"] = True

	def sayFailureMessage(self, topic):
		self.spies["sayFailureMessage"] = True

	def saveAttributeInSession(self, attribute, value):
		self.session[attribute] = value


if __name__ == '__main__':
    unittest.main()