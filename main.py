#!/usr/bin/env python3

import pandas as pd
import requests
import datetime
import os

today = datetime.date.today()

table = f"TABLE{today.year}{today.month:02}"
df = pd.read_html(f'{os.getenv("LABEL")}{os.getenv(table)}')[0]

challenge_number = (today-datetime.date(2023,10,31)).days
is_today = (df.iloc[:,1] == str(today.day)).values
conf = df.iloc[is_today, 2:6].values[0]

message = f"__**GPC Daily Challenge #{challenge_number}**__\nMap: **{conf[0]}**\nSettings: {conf[1]}, {conf[2]}\n<{conf[3]}>\n<@&1172389612665180190>"
json_message={"content":message,}

#response = requests.post(os.getenv("WEBHOOK"),json=json_message)
#
#if response.status_code == 204:
#    print("Message sent successfully!")
#else:
#    print(f"Failed to send message: {response.status_code}")

if not (response := requests.post(os.environ["WEBHOOK_DEBUG"],json={"content":f"table is {table} \n os.getenv(table) is {os.getenv(table)} \n df.to_string() is {df.to_string()}",})).status_code == 204:
    raise Exception(f"Failed to send message: {response.status_code}")
