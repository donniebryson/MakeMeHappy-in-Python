# This is as simple a Python script as possible. 
# It seeks to fulfill the same user story as the Machine Learning for Kids worksheet
# 'Make me happy' which is written in Scratch. 

# It assumes that a class has already completed the project in Scratch on the
# website: https://machinelearningforkids.co.uk/#!/worksheets 
# If the Scratch version of the worksheet is complete, then the student has a workspace_id, username, and password for Watson.
# The student must have their model created and tested. These are needed for this script to work.

# The file, example_config_file.txt, must be edited to include your actual workspace_id, username, and password and then renamed
# config.json in the same direcory as MakeMeHappy.py.

# Each student will need to execute 'pip install watson_developer_cloud' for the proper Watson library. 

# The code was testing with Python 3.6.

# All credit is given to Dale Lane for the fantastic job he did with Machine Learning for Kids without entangling him in any 
# of my mistakes potentially here. 
# Direct corrections and suggestions for this Python code to: donniebryson@gmail.com 

from watson_developer_cloud import AssistantV1
import json
import os
import sys

with open(os.path.dirname(os.path.abspath( __file__ )) + r"\config.json") as my_config:
    my_json_config = json.loads(my_config.read())

watson_assistant = AssistantV1(
    version='2018-02-16',
    username=my_json_config['username'], 
    password=my_json_config['password'], 
)


def GetOpinion():
    line = input("What do you think of me? ");
    return line;

class MachineLearningHandTooled:
    """Hand Tooled Machine Learning Class"""

    def load(self):
        with open(os.path.dirname(os.path.abspath( __file__ )) + r"\keywords.json") as my_data:
            my_json_data = json.loads(my_data.read())
            self.happy = my_json_data['happy']
            self.sad = my_json_data['sad']

    def __init__(self):
        self.happy = ["pretty", "smart", "friendly"]
        self.sad = ["ugly", "dumb", "mean"]
        self.load()
    

    def guess(self, s):
        happyCount = 0
        sadCount = 0
        for h in self.happy:
            if h in s:
                happyCount += 1
        for sw in self.sad:
            if sw in s:
                sadCount += 1
        if happyCount > sadCount:
            return "happy"
        elif sadCount > happyCount:
            return "sad"
        else:
            return "unknown"
        
class MachineLearningWatson:    
    """Machine Learning Class using Watson"""

    def __init__(self):
        pass
    
    def load(self):
        pass

    def guess(self, s):
        response = watson_assistant.message(
            workspace_id=my_json_config['workspace_id'], 
            input={
                'text': s
            }
        )   
        # Never assume you are going to get valid input
        if response['intents'] is None or response['intents'] == []:
            r = 'unknown'
        elif response['intents'][0]['intent'] == 'happy':
            r = 'happy'
        else:
            r = 'sad'
        return r
 
if my_json_config['watson'] == "no":
    ml_engine = MachineLearningHandTooled()
else:
    ml_engine = MachineLearningWatson()

line = GetOpinion()
res = ml_engine.guess(line)

if ( res == "happy"):
    print("Your kindness has made me happy.")
elif ( res == "sad"):
    print("Your rudeness has mad me sad.")
else:
    print("I do not know what you think.")
