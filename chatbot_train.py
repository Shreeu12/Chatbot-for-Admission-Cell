
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os



def setup():
   chatbot = ChatBot('Bot', 
    storage_adapter='chatterbot.storage.SQLStorageAdapter', 
   trainer='chatterbot.trainers.ListTrainer')



for file in os.listdir('D:/DYP-ATU Chabot/data/'):
        convData = open(r'D:/DYP-ATU Chabot/data/' + file, encoding='latin-1').readlines()
        chatbot.set_trainer(ListTrainer)
        chatbot.train(convData)

	print("Training completed")
  #This line prints the message "Training completed" to the console after the training process is finished. 

setup()
#This line calls the setup() function, initiating the training process for the chatbot.
