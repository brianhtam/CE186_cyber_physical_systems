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
serial_port_name = '/dev/cu.usbserial-DN01YUME' 
ser = serial.Serial(serial_port_name,9600,timeout=1)
base = 'http://127.0.0.1:5000'
network_id = 'local'
header = {}


# Delete Existing Arduino Object
query = {}
endpoint = '/networks/'+network_id+'/objects/Arduino'
response = requests.request('DELETE', base + endpoint, params=query, headers=header, timeout=120 )
resp = json.loads( response.text )
if resp['object-code'] == 200:
 print('I Deleted Arduino')
else:
 print('I Did Not Delete Arduino')
 print( response.text )


# Delete Received Object
query = {}
endpoint = '/networks/'+network_id+'/objects/ReceivedData'
response = requests.request('DELETE', base + endpoint, params=query, headers=header, timeout=120 )
resp = json.loads( response.text )
if resp['object-code'] == 200:
 print('Deleted ReceivedData')
else:
 print('Did Not Delete ReceivedData')
 print( response.text )



# Create Arduino Object
query = {
 'object-name': 'Arduino'
 }
endpoint = '/networks/'+network_id+'/objects/Arduino'
response = requests.request('PUT', base + endpoint, params=query,headers=header, timeout=120 )
resp = json.loads( response.text )
if resp['object-code'] == 201:
 print('Create object Arduino: ok')
else:
 print('Create object Arduino: error')
 print( response.text )


# Create ReceivedData Object
query = {
 'object-name': 'ReceivedData'
}
endpoint = '/networks/'+network_id+'/objects/ReceivedData'
response = requests.request('PUT', base + endpoint, params=query, headers=header, timeout=120 )
resp = json.loads( response.text )
if resp['object-code'] == 201:
 print('Create object ReceivedData: ok')
else:
 print('Create object ReceivedData: error')
 print( response.text )


# Create ReceivedData Stream
query = {
 'stream-name': 'ReceivedDataStream',
 'points-type': 'i' # 'i', 'f', or 's'
}
endpoint = '/networks/'+network_id+'/objects/ReceivedData/streams/ReceivedDataStream'
response = requests.request('PUT', base + endpoint, params=query, headers=header, timeout=120 )
resp = json.loads( response.text )
if resp['stream-code'] == 201:
 print('Create stream ReceivedDataStream: ok')
else:
 print('Create stream ReceivedDataStream: error')
 print( response.text )


# Create VOC stream
query = {
 'stream-name': 'VOC',
 'points-type': 'i' # 'i', 'f', or 's'
}
endpoint = '/networks/'+network_id+'/objects/Arduino/streams/VOC'
response = requests.request('PUT', base + endpoint, params=query, headers=header, timeout=120 )
resp = json.loads( response.text )
if resp['stream-code'] == 201:
 print('Create stream VOC: ok')
else:
 print('Create stream VOC: error')
 print( response.text )


# Create CO2 Stream
query = {
 'stream-name': 'CO2',
 'points-type': 'i' # 'i', 'f', or 's'
}
endpoint = '/networks/'+network_id+'/objects/Arduino/streams/CO2'
response = requests.request('PUT', base + endpoint, params=query,
headers=header, timeout=120 )
resp = json.loads( response.text )
if resp['stream-code'] == 201:
 print('Create stream Temperature: ok')
else:
 print('Create stream Temperature: error')
 print( response.text )

# Create Temperature Stream
query = {
 'stream-name': 'Temperature',
 'points-type': 'i' # 'i', 'f', or 's'
}
endpoint = '/networks/'+network_id+'/objects/Arduino/streams/Temperature'
response = requests.request('PUT', base + endpoint, params=query,
headers=header, timeout=120 )
resp = json.loads( response.text )
if resp['stream-code'] == 201:
 print('Create stream Temperature: ok')
else:
 print('Create stream Temperature: error')
 print( response.text )

# Create Humidity Stream
query = {
 'stream-name': 'Humidity',
 'points-type': 'i' # 'i', 'f', or 's'
}
endpoint = '/networks/'+network_id+'/objects/Arduino/streams/Humidity'
response = requests.request('PUT', base + endpoint, params=query,
headers=header, timeout=120 )
resp = json.loads( response.text )
if resp['stream-code'] == 201:
 print('Create stream Humidity: ok')
else:
 print('Create stream Humidity: error')
 print( response.text )

# Create PM Stream
query = {
 'stream-name': 'PM',
 'points-type': 'i' # 'i', 'f', or 's'
}
endpoint = '/networks/'+network_id+'/objects/Arduino/streams/PM'
response = requests.request('PUT', base + endpoint, params=query,
headers=header, timeout=120 )
resp = json.loads( response.text )
if resp['stream-code'] == 201:
 print('Create stream PM: ok')
else:
 print('Create stream PM: error')
 print( response.text )


delay = 1*5 # Delay of 5 seconds


# Run once at the start
def setup():
 try:
     print "Setup"
 except:
     print "Setup Error"
 
    
    
 # Run continuously forever
def loop():
 # Check if something is in serial buffer
 if ser.inWaiting()>0:
     try:
 # Read entire line until '\n'
         x=ser.readline()
 # Print points to Python to ensure receipt
         print "Received:", x
         print "Type:", type(x)
 # Parse input stream into appropriate values
         CO2,PM,VOC,Humidity,Temperature = splitdata(x)
         print CO2
         print PM
         print VOC
         print Humidity
         print Temperature 

 # Post (append) values into appropriate streams' points
         print("Start sending State point (Ctrl+C to stop)")
         endpoint ='/networks/local/objects/Arduino/streams/CO2/points'
         query = {'points-value': CO2,
                  'points-at': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
 }
         response = requests.request('POST', base + endpoint, params=query, headers=header, timeout=120 )
         resp = json.loads( response.text )
         
         if resp['points-code'] == 200:
             print( 'Update CO2 points: ok')
         else:
            print( 'Update CO2 points: error')
            print( response.text )

# Post (append) values into appropriate streams' points
         print("Start sending State point (Ctrl+C to stop)")
         endpoint ='/networks/local/objects/Arduino/streams/PM/points'
         query = {'points-value': PM,
                  'points-at': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
 }
         response = requests.request('POST', base + endpoint, params=query, headers=header, timeout=120 )
         resp = json.loads( response.text )
         
         if resp['points-code'] == 200:
             print( 'Update PM points: ok')
         else:
            print( 'Update PM points: error')
            print( response.text )        
        
# Post (append) values into appropriate streams' points
         print("Start sending State point (Ctrl+C to stop)")
         endpoint ='/networks/local/objects/Arduino/streams/VOC/points'
         query = {'points-value': VOC,
                  'points-at': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
 }
         response = requests.request('POST', base + endpoint, params=query, headers=header, timeout=120 )
         resp = json.loads( response.text )
         
         if resp['points-code'] == 200:
             print( 'Update VOC points: ok')
         else:
            print( 'Update VOC points: error')
            print( response.text )        

# Post (append) values into appropriate streams' points
         print("Start sending State point (Ctrl+C to stop)")
         endpoint ='/networks/local/objects/Arduino/streams/Humidity/points'
         query = {'points-value': Humidity,
                  'points-at': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
 }
         response = requests.request('POST', base + endpoint, params=query, headers=header, timeout=120 )
         resp = json.loads( response.text )
         
         if resp['points-code'] == 200:
             print( 'Update Humidity points: ok')
         else:
            print( 'Update Humidity points: error')
            print( response.text )        
        
# Post (append) values into appropriate streams' points
         print("Start sending State point (Ctrl+C to stop)")
         endpoint ='/networks/local/objects/Arduino/streams/Temperature/points'
         query = {'points-value': Temperature,
                  'points-at': datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%fZ")
 }
         response = requests.request('POST', base + endpoint, params=query, headers=header, timeout=120 )
         resp = json.loads( response.text )
         
         if resp['points-code'] == 200:
             print( 'Update Temperature points: ok')
         else:
            print( 'Update Temperature points: error')
            print( response.text )        
     except:
            print "Error"
 time.sleep(0.01) 
 return
 

# Run forever
# with a delay between calls
def delayed_loop():
 print "Delayed Loop"
 # Retrieve most recent ReceivedData value
 print("Start retrieving ReceivedData point")
 query = {}
 endpoint ='/networks/'+network_id+'/objects/ReceivedData/streams/ReceivedDataStream/points'
 response = requests.request('GET', base + endpoint, params=query,headers=header, timeout=120 )
 resp = json.loads( response.text )
 ReceivedData = resp['points'][0]['value']
 print "Done Retrieving ReceivedData: ", ReceivedData
 # Send ReceivedData data to Arduino
 ReceivedData = str(ReceivedData)
 print "Type of ReceivedData: ",type(ReceivedData)
 ser.write(ReceivedData.encode("utf-8"))

# Run once at the end
def close():
 try:
     print "Close Serial Port"
     ser.close()

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
 # Call close function
 close()


#Function to partition input
def splitdata( x ):
  mylist = x.split(',')
  CO2Data = mylist[0]
  PMData = mylist[1]
  VOCData = mylist[2]
  HumidityData = mylist[3]
  TemperatureData = mylist[4]
  return int(CO2Data),int(PMData), int(VOCData), int(HumidityData), int(TemperatureData)
# Run the program
main()




