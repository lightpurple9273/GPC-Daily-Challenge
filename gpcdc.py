#!/usr/bin/env python3

import pandas as pd
import requests
import datetime
import os

class Tables:
    def __init__(self):
        self.dfs = {}
        
    def read(self,datetime_date):
        key = f"TABLE{datetime_date.year}{datetime_date.month:02}"
        if key not in self.dfs:
            self.dfs[key] = pd.read_html(f'{os.environ["LABEL"]}{os.environ[key]}')[0]
        return self.dfs[key]

class Announcement:
    def __init__(self):
        pass

    def create_message(self,datetime_date,tables,pre_message="",post_message="",suppress_ping=bool(False),raise_if_corruption_detected=bool(False)):
        challenge_number = (datetime_date-datetime.date(2023,10,31)).days
        df = tables.read(datetime_date)
        is_today = (df.iloc[:,1] == str(datetime_date.day)).values
        conf = df.iloc[is_today, 2:6].values[0]

        if raise_if_corruption_detected:
            if not "https://www.geoguessr.com/challenge/" in conf[3]:
                raise Exception(f"URL is not set for {datetime_date}")
        
        self.message = f"{pre_message}__**GPC Daily Challenge #{challenge_number}**__\nMap: **{conf[0]}**\nSettings: {conf[1]}, {conf[2]}\n<{conf[3]}>"
        if not suppress_ping:
            self.message = f"{self.message}\n<@&1172389612665180190>"
        self.message = f"{self.message}{post_message}"
    
    def post(self,webhook_endpoint_url):
        self.response = requests.post(webhook_endpoint_url,json={"content":self.message,})
        if self.response.status_code == 204:
            print("Message sent successfully!")
        else:
            raise Exception(f"Failed to send message: {response.status_code}")

if __name__ == "__main__":
    tables = Tables()
    anun = Announcement()

    anun.create_message(datetime.date.today(),tables)
    print(anun.message)
    #anun.post(os.environ["WEBHOOK_DEVELOP"])
        
    anun.create_message(datetime.date.today()+datetime.timedelta(days=1),tables)
    print(anun.message)
    #anun.post(os.environ["WEBHOOK_DEVELOP"])


