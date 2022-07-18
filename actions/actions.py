# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from tokenize import Name
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet,UserUtteranceReverted, ActionReverted
from datetime import datetime, timedelta
from regex import P
import wikipedia
from Features.news import get_news
import webbrowser
from Features.alarm import set_alarm
from Features.joke import startJoke
from Features.weather import weather_from_city, weather_local
from Features.wishme import wishMe
from Features.object_detection import object_detection,get_object
from Features. navigation import navigation, get_direction
from sanic.config import Config
from Features.asia_landmarks import landmark_detection_with_address
from Features.get_image import get_image
from Features.text_detector import text_detector
from inference.video_classifier import face_recongizer
from Features.speak import speak
from Features.listen import listen
from Features.FaceRecognition import FaceRecognition
from Features.csv_writer import prev_response
import os
Config.KEEP_ALIVE_TIMEOUT = 60
Config.KEEP_ALIVE = False
try:
    import pywhatkit
except Exception as e:
    print("Exception: ", e)


def pywhatkit_search(query):
    query = str(query).replace("google", "").replace("search", "").replace("","").replace("what is","").replace("search about","").replace("search for","").replace("find","").replace("about","").replace("for","").replace("tell me ", "").replace("tell me something about ","").replace("tell", "")
    try:
               
                print("Going for Pywhatkit google search instead")
                pywhatkit.search(query)
    except Exception as e:
                print("Exception: ", e)
                print("Pywhatkit search failed...!!")
def dict_to_word(dict):
    word = ""
    for key, value in dict.items():
        word += key + ": " + value + " "
    return word



class ActionFallBack(Action):

    def name(self) -> Text:
        return "action_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            
            dispatcher.utter_message(text="Sorry, I didn't get that. Can you please rephrase it?")
            """
            A proper approach to implement this would be to have a fallback action by listing all the things that the bot can do. by using the buttons
            """

class ActionRepeat(Action):

    def name(self) -> Text:
        return "action_repeat"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            print("Entered Repeat action")
            dispatcher.utter_message(text= prev_response('response','logs\speak_logs.csv'))

class ActionFaceRecognition(Action):

    def name(self) -> Text:
        return "action_face_recognition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
            print("Entered Face Recognition action")
            FaceRecognition()
            
            
            
            
          
           
         

            
            
        

               
            
                
            
            
            



























# class YourResidence(Action):

#     def name(self) -> Text:
#         return "action_your_residence"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(template="utter_your_residence")

#         return [UserUtteranceReverted(), ActionReverted()] # By doing this we are basically asking our bot to forgot the last user utterance and to revert the last action. Basiscally we are making it forget that any such thing happened.

