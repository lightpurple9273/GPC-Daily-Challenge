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
            if os.getenv(key) is None:
                raise Exception(f"{key} is not set.")
            else:
                self.dfs[key] = pd.read_html(f'{os.getenv("LABEL")}{os.getenv(key)}')[0]
        return self.dfs[key]

    def mass_read(self):
        for year in range(2013,int(datetime.date.today().year)+int(11)):
            for month in range(1,13):
                table_of_the_month = f"TABLE{year}{month:02}"
                if os.getenv(table_of_the_month) is not None:
                    self.dfs[f"{year}{month:02}"] = pd.read_html(f'{os.getenv("LABEL")}{os.getenv(table)}')[0]

class Announcement:
    def __init__(self):
        pass

    def create_message(self,datetime_date,tables):
        challenge_number = (datetime_date-datetime.date(2023,10,31)).days
        df = tables.read(datetime_date)
        is_today = (df.iloc[:,1] == str(datetime_date.day)).values
        conf = df.iloc[is_today, 2:6].values[0]
        self.message = f"__**GPC Daily Challenge #{challenge_number}**__\nMap: **{conf[0]}**\nSettings: {conf[1]}, {conf[2]}\n<{conf[3]}>\n<@&1172389612665180190>"
    
    def post(self,webhook_endpoint_url):
        self.response = requests.post(webhook_endpoint_url,json={"content":self.message,})
        if self.response.status_code == 204:
            print("Message sent successfully!")
        else:
            raise Exception(f"Failed to send message: {response.status_code}")

if __name__ == "__main__":
    tables = Tables()
    an = Announcement()

    an.create_message(datetime.date.today(),tables)
    print(an.message)
    #an.post(os.getenv("WEBHOOK_DEVELOP"))
        
    an.create_message(datetime.date.today()+datetime.timedelta(days=1),tables)
    print(an.message)
    #an.post(os.getenv("WEBHOOK_DEVELOP"))


