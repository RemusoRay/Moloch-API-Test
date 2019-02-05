# Courtesy of Dom A. Richardson

# importing requests, csv, datetime packages
# needed to pip install requests

import requests
# import pandas


# import csv
from requests.auth import HTTPDigestAuth
import datetime

# http://docs.python-requests.org/en/master/
# requests package documentation

# https://github.com/aol/moloch/wiki/API

# set web authentication credentials
MOLOCH_USER = 'test'
MOLOCH_PASSWORD = 'XXXXXXX'

# set variables for get request to moloch, need to make it so select from menu

exp = input("Expression? [srcIp] [dstIp]: ")

# Create start and stop time inputs, convert to epoch time, and convert epoch time from float to integer
start_time = input("Start time? (YYYY-MM-DD HH:MM:SS): ")
start_epoch_time = datetime.datetime.strptime("%s" % start_time, "%Y-%m-%d %H:%M:%S").timestamp()
start_epoch_time = int(start_epoch_time)


stop_time = input("Stop time? (YYYY-MM-DD HH:MM:SS): ")
stop_epoch_time = datetime.datetime.strptime("%s" % stop_time, "%Y-%m-%d %H:%M:%S").timestamp()
stop_epoch_time = int(stop_epoch_time)



# basic GET request with variables for putting in different stuff
# test r = requests.get('http://xxx.xxx.xxx.xxx:8005/unique.txt?exp=protocol&counts=1&stopTime=1549157290&startTime=1549156854', auth=HTTPDigestAuth(MOLOCH_USER, MOLOCH_PASSWORD))

r = requests.get(("http://xxx.xxx.xxx.xxx:8005/unique.txt?exp=%s&counts=1&stopTime=%d&startTime=%d" % (exp, stop_epoch_time, start_epoch_time)), auth=HTTPDigestAuth(MOLOCH_USER, MOLOCH_PASSWORD))

print(r.text)
print(r.status_code)
print(start_epoch_time)
print(stop_epoch_time)

# write each line into the CSV file (https://docs.python.org/3/library/functions.html#open)
with open('csvfile.csv', 'wb') as file:
    for l in r:
        file.write(l)
