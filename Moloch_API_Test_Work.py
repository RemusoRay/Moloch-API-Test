#!/usr/bin/env python3

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
MOLOCH_USER = 'anonymous'
MOLOCH_PASSWORD = 'XXXXXXX'

# Print welcome text
print("Welcome to the Auto Baseline Tool")

# Menu to set variables for the get request to moloch
options = {}
options['1'] = ("Source IP","srcIp")
options['2'] = ("Destination IP","dstIp")
options['3'] = ("Protocols","protocol")
options['4'] = ("HTTP Hostnames","http.host")


for entry in options:
    print(entry[0], options[entry][0])
selection = input("Please select: ")
if selection in options:
    exp = options[selection][1]
else:
    print("Unknown option selected")



# Create start and stop time inputs, and convert to epoch time
start_time = input("Start time? (YYYY-MM-DD HH:MM:SS): ")
start_epoch_time = datetime.datetime.strptime("%s" % start_time, "%Y-%m-%d %H:%M:%S").timestamp()
start_epoch_time = int(start_epoch_time)

stop_time = input("Stop time? (YYYY-MM-DD HH:MM:SS): ")
stop_epoch_time = datetime.datetime.strptime("%s" % stop_time, "%Y-%m-%d %H:%M:%S").timestamp()
stop_epoch_time = int(stop_epoch_time)

# basic get request with variables for putting in different stuff
# test r = requests.get('http://xxxxxxxxxxxxxxx:8005/unique.txt?exp=protocol&counts=1&stopTime=1549157290&startTime=1549156854', auth=HTTPDigestAuth(MOLOCH_USER, MOLOCH_PASSWORD))

# known good w/ auth r = requests.get(("http://localhost:8005/unique.txt?exp=%s&counts=1&stopTime=%d&startTime=%d" % (exp, stop_epoch_time, start_epoch_time)), auth=HTTPDigestAuth(MOLOCH_USER, MOLOCH_PASSWORD))

r = requests.get("http://localhost:8005/unique.txt?exp=%s&counts=1&stopTime=%d&startTime=%d" % (exp, stop_epoch_time, start_epoch_time))

# outputs and debug
print(r.text)
print(r.status_code)
print(start_epoch_time)
print(stop_epoch_time)

# write each line into the CSV file (https://docs.python.org/3/library/functions.html#open)
#with open('csvfile.csv', 'wb') as file:
#    for l in r:
#        file.write(l)


