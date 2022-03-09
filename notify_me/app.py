from git_history import History
import os

BASE_DIR = os.path.join(os.path.join(os.path.dirname(__file__), './data'))
history_file = os.path.join(BASE_DIR, 'history.csv')

if __name__ == "__main__":
    history = History()
    history.get_session()
    history.update_history(history_file)