# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Dict, Text, List, Any

from rasa_sdk import Tracker
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action
import datetime as dt
import smtplib

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_show_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
            currentTime=dt.datetime.now()
            timenow=currentTime.hour
    
            if timenow>=4 and timenow < 12:
                wish="Good morning."
                dispatcher.utter_message(text=f"Hello, {wish}. What can i help you? ")
                return []
            elif timenow>=12 and timenow < 16:
                wish="Good Afternoon"
                dispatcher.utter_message(text=f"Hello, {wish}. What can i help you? ")
                return []
            elif timenow>= 16 and timenow <= 18:
                wish="Good evening"
                dispatcher.utter_message(text=f"Hello, {wish}. What can i help you? ")
                return []
            else:
                dispatcher.utter_message(text=f"Hello, What can i help you? ")
                return []
            


class AskForSlotAction(Action):
    def name(self) -> Text:
        return "action_ask_get_detials"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        person_name = tracker.get_slot("person_name")
        job_function=tracker.get_slot("job_function")
        business_email=tracker.get_slot("business_email")
        company=tracker.get_slot("company")
        number=tracker.get_slot("number")
        use_case=tracker.get_slot("use_case")

        server= smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login('jagan.vijay.104@gmail.com','Jagan@1234')
        subject="Customer detials"
        body=f"Customer detials: \n Name: {person_name} \n Email id: {business_email} \n Phone number: {number} \n Company name: {company} \n Your job: {job_function}\n Use case: {use_case}"
        msg=f'Subject:{subject}\n\n{body}'
        server.sendmail('jagan.vijay.104@gmail.com','sivaneshkumar24@gmail.com',msg)
        print("Mail sended")
        

        dispatcher.utter_message(text=f"We will contant you soon {person_name}")
        return []

        

