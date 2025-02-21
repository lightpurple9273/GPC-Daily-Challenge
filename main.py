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
                    suppress_ping=bool(True),
                   pre_message="Tomorrow's DC announcement will be...\n====\n",
                   post_message="\n====\nA ping for `@GPC Daily Challenge`, role id 1172389612665180190, will be added for tomorrow.")
anun.post(os.getenv("WEBHOOK_DRAFT"))

if not (requests.post(os.getenv("WEBHOOK_LOG"),json={"content":"DC posting successful for today!",})).status_code == 204:
    raise Exception(f"Failed to send message: {response.status_code}")
    
