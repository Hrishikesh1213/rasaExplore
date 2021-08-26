# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

import requests,json
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_make_the_post"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # x = requests.get('https://jsonplaceholder.typicode.com/posts/1').json()

        cuisine = tracker.get_slot('cuisine')
        num_people = tracker.get_slot('num_people')

        dataobj = {
            'cuisine': cuisine,
            'num_people': num_people
        }
        z = requests.post('http://127.0.0.1:1880/server1', data = dataobj)
        # if z.status_code == 200:
        #     y = 'successfully posted'
        # else:
        #     y = json.dumps(x)
        dispatcher.utter_message(text=str(z.status_code))

        return []
