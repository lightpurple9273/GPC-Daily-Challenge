#!/usr/bin/env python3

import gpcdc

import requests

import datetime
import os

tables = gpcdc.Tables()
anun = gpcdc.Announcement()

anun.create_message(datetime.date.today(),tables)
anun.post(os.getenv("WEBHOOK_PUBLICATION"))
    
anun.create_message(datetime.date.today()+datetime.timedelta(days=1),tables,
                    supress_ping=bool(True),
                   pre_message="Tomorrow's DC announcement will be...\n====\m",
                   post_message="\n====\nA ping will be added for tomorrow.")
anun.post(os.getenv("WEBHOOK_DRAFT"))

response = requests.post(os.getenv("WEBHOOK_LOG"),json={"content":"DC posting successful for today!",})
if response.status_code == 204:
    print("Message sent successfully!")
else:
    raise Exception(f"Failed to send message: {response.status_code}")
    
