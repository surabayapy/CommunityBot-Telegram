import json
import os
import requests
import time
from dotenv import load_dotenv, find_dotenv

# load .env file
load_dotenv(find_dotenv())
bot_token = os.environ.get("BOT_TOKEN")
chat_ID = os.environ.get("CHAT_ID")


# function for send message to User or GroupChat
def sendMessage(chatID, text):
    parameter = {'chat_id': chatID, 'text': text}
    message = requests.post(bot_token + 'sendMessage', data=parameter)
    return message


# # function for check user profile photos (temporary disabled)
# def checkPhotoProfile():
#     parameter = {'user_id': chat_ID}
#     sendMessage(chat_ID, "halo kawan!")  # send message "halo kawan!"
#     getUserPhotoProfile = requests.post(
#         bot_token + 'getUserProfilePhotos', data=parameter)
#     sendMessage(chat_ID, getUserPhotoProfile)  # send message from return API

def job():
    while True:
        message = requests.get(bot_token + 'getUpdates')
        messageJSON = json.loads(message.text)
        try:
            messageText = messageJSON['result'][-1]['message']['text']
            userName = messageJSON['result'][-1]['message']['from']['first_name']
            if messageText == "/start@surabayapy_bot":
                sendMessage(
                    chat_ID, "Halo,{}! tekan masukkan perintah /antispam untuk mengaktifkan fitur antispam :D".format(userName))

                while True:
                    message = requests.get(bot_token + 'getUpdates')
                    messageJSON = json.loads(message.text)
                    messageText = messageJSON['result'][-1]['message']['text']
                    print("menunggu perintah")
                    time.sleep(1)
                    if messageText == "/antispam@surabayapy_bot":
                        sendMessage(chat_ID, "fitur antispam telah diaktifkan")
                        return

        except KeyError:
            pass


# for a while, the main program like this
if __name__ == "__main__":
    sendMessage(chat_ID, "bot activated . .")
    sendMessage(chat_ID, "kirimkan perintah /start untuk memulai")
    job()
