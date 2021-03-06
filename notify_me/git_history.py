from requests_html import HTMLSession
from bs4 import BeautifulSoup
from datetime import datetime
from config import crawl_config
import pandas as pd
import os

class History(object):
        
    def __init__(self):
        self._url = crawl_config['url']
        self._headers = crawl_config['headers']
        self._params = crawl_config['params']
        self._connection = False
        self._html = None
        self._soup = None

    def get_session(self):
        
        with HTMLSession() as s:
            try:
                res = s.get(self._url, headers=self._headers, timeout=5.0)
                soup = BeautifulSoup(res.content, 'html.parser')
            except Exception as e:
                print("Connection Error Occured")
                raise e
            else:
                self.connection = True
                self.html = res
                self.soup = soup
        return                 
                                
    def get_commit_history(self):
        
        assert self.html and self.soup
                                
        commit_lst = self.soup.find_all("rect", {"class": "ContributionCalendar-day"})
        commit_lst = [c for c in commit_lst if c.get("data-date")]

        info_list = []
        dates = []

        for commit in commit_lst:

            dates.append(commit.get("data-date"))
            info = {
                "commit_cnt": commit.get("data-count")
            }
            info_list.append(info)

        return dates, info_list
    
    def get_today_commit_info(self):

        assert self.html and self.soup

        today = datetime.today().strftime("%Y-%m-%d")           
        commit_comp = self.soup.find("rect", {"data-date" : today})
        msg = None

        if commit_comp:
            commit_cnt = int(commit_comp.get('data-count'))
            if  commit_cnt == 0:
                msg = "Commit Not Updated Today"
            else:
                msg = "Commit Updated Today"
        
        return msg
                                
                                
    def update_history(self, save_path):

        date, info = self.get_commit_history()
        df = pd.DataFrame(data=info, index=date)
        
        # History not exists
        if not os.path.exists(save_path):

            with open(save_path, 'a') as f:
                df.to_csv(f, header=False)
            
        # History already exists
        else:
            # append history
            pass
