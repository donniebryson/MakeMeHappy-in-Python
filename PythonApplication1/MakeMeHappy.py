# This is as simple a Python script as possible. 
# It seeks to duplicate the function in the Machine Learning for Kids project
# 'Make me happy' which is written in Scratch. 

# It assumes that a class has already completed the project in Scratch on the
# website: https://machinelearningforkids.co.uk/#!/worksheets 
# If the Scratch version of the worksheet is complete, then the student has a workspace_id, username, and password for Watson.
# The student also has their model created and tested. 

# All credit is given to Dale Lane for the fantastic job he did with Machine Learning for Kids without intangling him in any 
# of my mistakes potentially here.

from watson_developer_cloud import AssistantV1
import json


watson_assistant = AssistantV1(
    version='2018-02-16',
    username='6d6cc51c-d711-4f2e-b717-aba62f1949eb',
    password='Cc4hKrzGpjjg'
)


def GetOpinion():
    line = input("What do you think of me? ");
    return line;

def CheckResponse(r):
    response = watson_assistant.message(
        workspace_id='937c9d3b-1683-44fe-95d2-fd3a8d22c6c8',
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

