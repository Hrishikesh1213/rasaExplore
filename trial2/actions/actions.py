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

from twilio.rest import Client 

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_post_data"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        cuisine = tracker.get_slot('cuisine')
        num_people = tracker.get_slot('num_people')
        # slot_number = tracker.get_slot('slot_number')

        # account_sid = "AC90e2d0be773c5e1eb80153cfe65b7221"
        # auth_token =  "3af6d18255b49d61a6a83a070430681f"
        # client = Client(account_sid, auth_token) 

        # sender = 'whatsapp:+14155238886'
        # reciever = 'whatsapp:+919381567454'

        # URL = "https://jsonplaceholder.typicode.com/posts/{0}".format(slot_number)

        dataobj = {
            'cuisine': cuisine,
            'num_people': num_people
        }
        z = requests.post('http://127.0.0.1:1880/server1', data = dataobj)
        # x = requests.get(URL).json()
        # y = json.dumps(x)
        
        dispatcher.utter_message(text=str(z.status_code))

        return []
