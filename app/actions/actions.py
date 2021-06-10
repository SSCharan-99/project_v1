# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher




class Actionpackage(Action):

    def name(self) -> Text:
        return "action_package"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities=tracker.latest_message['entities']
        print(entities)
        
        for e in entities:
            if e['entity'] == 'year':
                name = e['value']
            if name == "2020":
                message="highest package is 24L <a href='https://www.msitprogram.net/'>For more info click here</a>"
            if name == "2019":
                message="highest package is 22L"
            if name == "2018":
                message="highest package is 20L"
        #dispatcher.utter_message(text="Hello World!")
        
        dispatcher.utter_message(text=message)

        return []

class Actionfee(Action):

    def name(self) -> Text:
        return "action_fee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities=tracker.latest_message['entities']
        print(entities)
        msg="Fee"
        for e in entities:
            
            if e['entity'] == 'institute':
                name = e['value']
            if name == "JNTUH":
                msg="Fee at JNTUH is 170000"
            if name == "IIIT":
                msg="Fee at IIITH is 200000"
            if name == "JNTUK":
                msg="Fee at JNTUK is 130000"
            if name == "SVU":
                msg="Fee at SVU is 130000"
        #dispatcher.utter_message(text="Hello World!")
        
        dispatcher.utter_message(text=msg)

        return []