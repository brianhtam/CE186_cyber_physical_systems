#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author: pan
"""

import requests
import json
import time
import datetime
import serial
from flask import Flask, request, jsonify
# Change the port name to match the port to which your Arduino is connected
serial_port_name = '/dev/cu.usbserial-DN01YUME' #for mac
ser = serial.Serial(serial_port_name,9600,timeout=1)
base = 'http://127.0.0.1:5000'

network_id = 'local'
header = {}
delay = 1*5 # Delay in seconds



# Run once at the start
def setup():
 try:
     print "Setup"

 except:
     print "Setup Error"
     
 
 
 
# Run continuously forever
def loop():
 # Retrieve most recent State value
 query = {}
 endpoint ='/networks/'+network_id+'/objects/Arduino/streams/CO2/points'
 response = requests.request('GET', base + endpoint, params=query, headers=header, timeout=120 )
 resp = json.loads( response.text )
 CO2 = resp['points'][0]['value']

 if CO2 > 10: #UPDATED

     output = 230

 # Post (append) values into appropriate streams' points
 
     print("Start sending ReceivedData point (Ctrl+C to stop)")
     endpoint ='/networks/local/objects/ReceivedData/streams/ReceivedDataStream/points'

     query = {
             'points-value': output,
             'points-at': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
 }
     response = requests.request('POST', base + endpoint, params=query, headers=header, timeout=120 )
     resp = json.loads( response.text )
     if resp['points-code'] == 200:
         print( 'Update ReceivedData points: ok')
     else:
         print( 'Update ReceiedData: error')
         print( response.text )
         
         
 else:
     output = 130
     print("Start sending ReceivedData point (Ctrl+C to stop)")
     endpoint = '/networks/local/objects/ReceivedData/streams/ReceivedDataStream/points'
     query = {
             'points-value': output,
             'points-at': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
 }
     response = requests.request('POST', base + endpoint, params=query, headers=header, timeout=120 )
     resp = json.loads( response.text )
     
     if resp['points-code'] == 200:
         print( 'Update ReceivedData points: ok')
     else:
         print( 'Update ReceiedData: error')
         print( response.text )

 # 5 Second Delay
 time.sleep(5) #Make GET requests to the server every 5 seconds
 return

# Run continuously forever
# with a delay between calls
def delayed_loop():
 print "Delayed Loop"

# Run once at the end
def close():
 try:
     print "Close"
 except:
     print "Close Error"
     
     
     
# Program Structure
def main():
 # Call setup function
 setup()
 # Set start time
 nextLoop = time.time()
 while(True):
 # Try loop() and delayed_loop()
     try:
         loop()
         if time.time() > nextLoop:
 # If next loop time has passed...
             nextLoop = time.time() + delay
             delayed_loop()
     except KeyboardInterrupt:
 # If user enters "Ctrl + C", break while loop
         break
     except:
 # Catch all errors
         print "Unexpected error."
         time.sleep(5) #to keep error messages from imploding
 # Call close function
 close()
 
# Run the program
main()