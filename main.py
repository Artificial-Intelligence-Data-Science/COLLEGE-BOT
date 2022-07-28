
import requests
import os
from Features.wishme import wishMe
from Features.csv_writer import append_data
from Features.speak import speak
from Features.listen import listen_std
from Features.time_checker import inactive
from Features.read_logs import read_logs
import time



sender = "Prajwal"
bot_name = "DISHA"
bot_message = ""
user = ""
append_data("logs/chat_logs.csv","entered", "entered")
print("Hello, Welcome to the department of Artificial Intelligence and Data Science")
choice = input("Would you like to continue?")
if choice == "yes":
    speak(wishMe())
    os.system('start cmd /k start\\face_recog_wo_speak.cmd')
    while True:
        print("__________The status is inactive___________")
        print(f"call my name ({bot_name}) to resume")
        query = listen_std()
        if f"{bot_name.lower()}" in query:
            status = True
            append_data('data.csv',"Entered", "Entered")
            while status == True:
                print("__________The status is active___________")
                print("Ask me anything now")
                user_message = listen_std()
                if len(user_message) != 0:
                    print("Sending message now....")
                    r = requests.post("http://localhost:5005/webhooks/rest/webhook", json={"sender": sender, "message": user_message})
                    print("Bot: ", end = ' ')
                    user = read_logs("logs/initial_face_logs.csv", "user")
                   
                    for i in r.json():
                        try:
                            bot_message = i["text"]
                            bot_message = bot_message.replace("sir",user).replace("Sir",user)
                            speak(bot_message)
                            append_data("logs/chat_logs.csv", user_message,bot_message ) 
                        except Exception as e:
                            print("Exception: ", e)
                            for content in i.keys():
                                speak(i[content])
                                append_data("logs/chat_logs.csv", user_message,i[content] )
                status = inactive('logs/chat_logs.csv', 30)
    
