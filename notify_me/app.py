import os
from git_history import History
from slack_api.notice import notice_message
from slack_api.schedule import schedule
from config import post_config

BASE_DIR = os.path.join(os.path.join(os.path.dirname(__file__), './data'))
history_file = os.path.join(BASE_DIR, 'history.csv')

if __name__ == "__main__":
    history = History()
    history.get_session()

    git_msg = history.get_today_commit_info()
    # https://time.is/ko/Unix_time_converter

    # Schedule commit message using Slack API
    timestamp = "1646826378"
    schedule(git_msg, timestamp)
    
    # Post Message
    attach_list=[post_config]
    notice_message(git_msg, attach_list)