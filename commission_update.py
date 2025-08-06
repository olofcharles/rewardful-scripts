#!/usr/bin/env python
import csv
import requests
from requests.structures import CaseInsensitiveDict
import json
import time
from datetime import datetime, timedelta

# Ask for the API secret
api_secret = input("Enter API secret: ")
pause = int(input("How many seconds to pause? "))

api_key = (api_secret, "")

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

# Open CSV file, indicate the file name as the first argument of the open function
with open('CSV FILENAME.csv', mode="r", encoding="utf-8-sig") as commissions_id:
    commissions = csv.reader(commissions_id)
    list_commissions = list(commissions)

counter = 0

for commission in range(len(list_commissions) - 1):
    comm_id = list_commissions[commission][0]
    comm_generated_date = datetime.strptime(list_commissions[commission][1], "%Y-%m-%dT%H:%M:%S.%f")
    new_due_date = comm_generated_date + timedelta(days=30)
    isoformat_new_due_date = new_due_date.strftime("%Y-%m-%dT%H:%M:%SZ")

    # Add the API endpoint parameters
    url = "https://api.getrewardful.com/v1/commissions/" + comm_id
    data = {
       "due_at": isoformat_new_due_date,
    }

    resp = requests.put(url, headers=headers, data=data, auth=api_key)
    status = resp.status_code

    if status == 200:
        print("Due date changed for commission ID: {}. Commission generation date: {}. New due date: {}".format(comm_id, comm_generated_date, isoformat_new_due_date))
        counter += 1
        print("Number of IDs processed: {}".format(counter))

    else:
        print("Due date for commission ID {} not changed".format(comm_id))

    print("Pausing for " + str(pause) + " second/s...")
    time.sleep(pause)

print("Total commissions updated: "+ str(counter))
