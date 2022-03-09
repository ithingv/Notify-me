# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
# https://api.slack.com/tutorials/tracks/scheduling-messages
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from config import slack_config

logger = logging.getLogger(__name__)

def schedule(msg, timestamp):

    token = slack_config['token']
    channel_id = slack_config['channel_id']
    client = WebClient(token=token)

    try:
    # Call the chat.scheduleMessage method using the WebClient
        result = client.chat_scheduleMessage(
            channel=channel_id,
            text= msg,
            post_at=timestamp
    )
        # Log the result
        logger.info(result)

    except SlackApiError as e:
        logger.error("Error scheduling message: {}".format(e))
