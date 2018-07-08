# This is as simple a Python script as possible. 
# It seeks to fulfill the same user story as the Machine Learning for Kids worksheet
# 'Make me happy' which is written in Scratch. 

# It assumes that a class has already completed the project in Scratch on the
# website: https://machinelearningforkids.co.uk/#!/worksheets 
# If the Scratch version of the worksheet is complete, then the student has a workspace_id, username, and password for Watson.
# The student also has their model created and tested. These are needed for this script to work.

# The file, example_config_file.txt, must be edited to include your actual workspace_id, username, and password and then renamed
# config.json in the same direcory as MakeMeHappy.py.

# Each student will need to execute 'pip install watson_developer_cloud' for the proper Watson library. 

# The code was testing with Python 3.6.

# All credit is given to Dale Lane for the fantastic job he did with Machine Learning for Kids without entangling him in any 
# of my mistakes potentially here. 
# Direct corrections and suggestions for this Python code to: donniebryson@gmail.com 

from watson_developer_cloud import AssistantV1
import json

with open("config.json") as my_config:
    my_json_config = json.loads(my_config.read())

watson_assistant = AssistantV1(
    version='2018-02-16',
    username=my_json_config['username'], 
    password=my_json_config['password'], 
)


def GetOpinion():
    line = input("What do you think of me? ");
    return line;

def CheckResponse(r):
    response = watson_assistant.message(
        workspace_id=my_json_config['workspace_id'], 
        input={
            'text': r
        }
    )
    # Never assume you are going to get valid input
    if response['intents'] is None or response['intents'] == []:
        r = 'unknown'
    elif response['intents'][0]['intent'] == 'happy':
        r = 'good'
    else:
        r = 'bad'
    # Let the person know if you are taking it as an insult or a complement
    if r == "good":
        print("You make me happy!");
    elif r == "bad":
        print ("You made me sad!");
    else:
        print ("Who knows what you think?");

CheckResponse(GetOpinion());

