import requests
import os
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


# function for check user profile photos
def checkPhotoProfile():
    parameter = {'user_id': chat_ID}
    sendMessage(chat_ID, "halo kawan!")  # send message "halo kawan!"
    getUserPhotoProfile = requests.post(
        bot_token + 'getUserProfilePhotos', data=parameter)
    sendMessage(chat_ID, getUserPhotoProfile)  # send message from return API


# for a while, the main program like this
if __name__ == "__main__":
    checkPhotoProfile()
