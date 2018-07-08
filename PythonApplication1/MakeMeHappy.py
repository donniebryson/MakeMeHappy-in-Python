# This is a simple python script
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
#    print(response);
    if response['intents'] == '':
        r = 'unknown'
    elif response['intents'][0]['intent'] == 'happy':
        r = 'good'
    else:
        r = 'bad'
    if r == "good":
        print("You make me happy!");
    elif r == "bad":
        print ("You made me sad!");
    else:
        print ("Who knows what you think?");

CheckResponse(GetOpinion());

