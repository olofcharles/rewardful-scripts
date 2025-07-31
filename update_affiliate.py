#!/usr/bin/env python

import requests
import requests
from requests.structures import CaseInsensitiveDict
import time
import csv

# Ask user for the API secret of the company asking for affiliate updating
api_secret = str(input("Enter API secret: "))
pause = int(input("How many seconds to pause? "))

# Initialize URL request variables
api_key = (api_secret,"")

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

# Open CSV file, indicate the file name as the first argument of the open function
with open('20250731-TERRAINONE-affiliates-delete-list.csv', mode="r", encoding="utf-8-sig") as affiliate_id:
    affiliates = csv.reader(affiliate_id)
    list_affiliate = list(affiliates)

affiliate_count = 0
print("Number of IDs: " + str(len(list_affiliate)))

# Iterate through the list of affiliate IDs.
for affiliate in range(len(list_affiliate) - 1):
    aff_id = list_affiliate[affiliate][0]
    url = "https://api.getrewardful.com/v1/affiliates/" + aff_id
    # Add the API endpoint parameters
    data = {
       "state": "disabled",
    }

    resp = requests.put(url, headers=headers, data=data, auth=api_key)
    status = resp.status_code

    if status == 200:
        print("Affiliate account disabled: " + aff_id)
        affiliate_count += 1
        print("Number of IDs processed: " + str(affiliate_count))

    else:
        print("Affiliate account NOT disabled: " + aff_id)

    print("Pausing for " + str(pause) + " second/s...")
    time.sleep(pause)

print("Total affiliates updated: "+ str(affiliate_count))
