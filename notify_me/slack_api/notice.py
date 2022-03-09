from config import slack_config
from config import post_config
import requests
import json

def notice_message(text, attachments):
    
    token = slack_config['token']
    channel = post_config['channel']

    attachments = json.dumps(attachments) # 리스트는 Json 으로 덤핑 시켜야 Slack한테 제대로 간다.
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+ token},
        data={"channel": channel, "text": text ,"attachments": attachments})