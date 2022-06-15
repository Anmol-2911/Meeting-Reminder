#!/usr/bin/env python3
from email_message import sending_email
from zenipy import calendar
subject="Meeting Reminder"
result=calendar(title="Meeting Reminder",text="When is the meeting?")
year,month,day=result
body="You have a meeting on {}/{}/{}".format(day,month,year)
sending_email(subject,body)
