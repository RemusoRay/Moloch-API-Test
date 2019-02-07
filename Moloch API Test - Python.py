#!/usr/bin/env python3

# Courtesy of Dom A. Richardson
# Testing getting multiple sets of data and writing them to xlsx

# http://docs.python-requests.org/en/master/
# requests package documentation

# https://github.com/aol/moloch/wiki/API

# importing requests, csv, datetime packages
# needed to pip install requests, xlsxwriter, xlrd
import requests
# import pandas
import csv
from requests.auth import HTTPDigestAuth
import datetime
import xlsxwriter
import xlrd

# set web authentication credentials if needed
MOLOCH_USER = 'test'
MOLOCH_PASSWORD = 'XXXXXXX'

# Print welcome text
print("Welcome to the Auto Baseline Tool")

# Menu to set variables for the get request to moloch
options = {}
options['1'] = ("Source IP", "srcIp")
options['2'] = ("Destination IP", "dstIp")
options['3'] = ("Protocols", "protocol")
options['4'] = ("HTTP Hostnames", "http.host")
options['5'] = ("Body Magic", "http.bodyMagic")
options['6'] = ("URI Paths", "http.path")

# Create start and stop time inputs, and convert to epoch time
start_time = input("Start time? (YYYY-MM-DD HH:MM:SS): ")
start_epoch_time = datetime.datetime.strptime("%s" % start_time, "%Y-%m-%d %H:%M:%S").timestamp()
start_epoch_time = int(start_epoch_time)

stop_time = input("Stop time? (YYYY-MM-DD HH:MM:SS): ")
stop_epoch_time = datetime.datetime.strptime("%s" % stop_time, "%Y-%m-%d %H:%M:%S").timestamp()
stop_epoch_time = int(stop_epoch_time)

# Write the data to Excel
row = 0
col = 0
workbook = xlsxwriter.Workbook("testworkbook.xlsx")
worksheet = workbook.add_worksheet()
for types in options:
    exp = options[types][1]
    r = requests.get(("http://192.168.1.X:8005/unique.txt?exp=%s&counts=1&stopTime=%d&startTime=%d" % (exp, stop_epoch_time, start_epoch_time)), auth=HTTPDigestAuth(MOLOCH_USER, MOLOCH_PASSWORD))
    r_converted = csv.reader(r.text.strip().split('\n'))
    worksheet.write(row, col, "%s" % options[types][0])
    worksheet.write(row, col + 1, "Counts")
    row += 1
    for line in r_converted:
        worksheet.write(row, col, line[0])
        worksheet.write(row, col+1, int(line[1]))
        row += 1
    col += 2
    row = 0

workbook.close()

print("Done!")
