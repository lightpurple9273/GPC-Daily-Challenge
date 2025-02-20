#!/usr/bin/env python3

import gpcdc

import datetime
import os

tables = gpcdc.Tables()
anun = gpcdc.Announcement()

#anun.create_message(datetime.date.today(),tables)
#print(anun.message)
#anun.post(os.getenv("WEBHOOK"))
    
anun.create_message(datetime.date.today()+datetime.timedelta(days=1),tables,supress_ping=bool(True))
#print(anun.message)
anun.post(os.getenv("WEBHOOK"))
