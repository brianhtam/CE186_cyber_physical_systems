"""
    IAQListenAndProcess
    John Stuart
    Retrieves data from the wallflower server, processes it, and sends results
    back to server
    
    Inputs: Arduino[PM,RH,Temp,VOC,CO2]
            User: BONUS: goals, period to average over
            Server: BONUS: SQL db list of space summaries
    Outputs: Data stream on 4 levels (min, hr, day, lifetime) with timestamps
             Rating for each data level if the average over X amount of time
                     exceeds recommended values (Good, Fair, Poor)
             Average Exposure for each pollutant
             Cumulative exposure over lifetime, past day, past hr, etc.
             % of time that has poor rating
             If poor, output instruction to display statistics and 
                 recommendations for a specific noncompliant pollutant.
             BONUS: Peaks to assess
             BONUS: average over a user determined range of time, so they can
                 test out a strategy for example and see the affect to 
                 cumulative exposure and % of poor time
             BONUS: Rank of a space comparing % poor time and average exposure
                 level
             
    
"""
# added sys.path block due to python error in finding correct file path
# import serial, json, and requests to read and send data to arduino and server
import sys  
#sys.path.append(r'C:\Python27\Lib\site-packages')
#import serial

sys.path.append(r'C:\Python27\Lib')
import json

sys.path.append(r'C:\Python27\Lib\site-packages\pip\_vendor')
import requests 

import time
import datetime
import random



delay = 5 # Delay in seconds

base = 'http://127.0.0.1:5000' 
network_id = 'local'
header = {}


############Delete/Recreate objects and streams

# Delete Result Object
query = {}
endpoint = '/networks/'+network_id+'/objects/result-object'
response = requests.request('DELETE', base + endpoint, params=query, headers=header, timeout=120 )
resp = json.loads( response.text )
if resp['object-code'] == 200:
 print('Deleted result-object')
else:
 print('Did Not Delete result-object')
 print( response.text )
 # Delete Hourly Object
query = {}
endpoint = '/networks/'+network_id+'/objects/hour-object'
response = requests.request('DELETE', base + endpoint, params=query, headers=header, timeout=120 )
resp = json.loads( response.text )
if resp['object-code'] == 200:
 print('Deleted hour-object')
else:
 print('Did Not Delete hour-object')
 print( response.text )
 # Delete Daily Object
query = {}
endpoint = '/networks/'+network_id+'/objects/day-object'
response = requests.request('DELETE', base + endpoint, params=query, headers=header, timeout=120 )
resp = json.loads( response.text )
if resp['object-code'] == 200:
 print('Deleted day-object')
else:
 print('Did Not Delete day-object')
 print( response.text )
 
 
 
 
 
# Create Result Object
query = {
 'object-name': 'result-object'
 }
endpoint = '/networks/'+network_id+'/objects/result-object'
response = requests.request('PUT', base + endpoint, params=query,headers=header, timeout=120 )
resp = json.loads( response.text )
if resp['object-code'] == 201:
 print('Create object result-object: ok')
else:
 print('Create object result-object: error')
 print( response.text )
# Create Hourly Object
query = {
 'object-name': 'hour-object'
}
endpoint = '/networks/'+network_id+'/objects/hour-object'
response = requests.request('PUT', base + endpoint, params=query, headers=header, timeout=120 )
resp = json.loads( response.text )
if resp['object-code'] == 201:
 print('Create object hour-object: ok')
else:
 print('Create object hour-object: error')
 print( response.text )
 # Create Daily Object
query = {
 'object-name': 'day-object'
}
endpoint = '/networks/'+network_id+'/objects/day-object'
response = requests.request('PUT', base + endpoint, params=query, headers=header, timeout=120 )
resp = json.loads( response.text )
if resp['object-code'] == 201:
 print('Create object day-object: ok')
else:
 print('Create object day-object: error')
 print( response.text )




# Create Result Stream
query = {
 'stream-name': 'result-stream',
 'points-type': 's' # 'i', 'f', or 's'
}
endpoint = '/networks/'+network_id+'/objects/result-object/streams/result-stream'
response = requests.request('PUT', base + endpoint, params=query, headers=header, timeout=120 )
resp = json.loads( response.text )
if resp['stream-code'] == 201:
 print('Create stream result-stream: ok')
else:
 print('Create stream result-stream: error')
 print( response.text )
 # Create Hourly Stream
query = {
 'stream-name': 'hour-stream',
 'points-type': 'i' # 'i', 'f', or 's'
}
endpoint = '/networks/'+network_id+'/objects/hour-object/streams/hour-stream'
response = requests.request('PUT', base + endpoint, params=query, headers=header, timeout=120 )
resp = json.loads( response.text )
if resp['stream-code'] == 201:
 print('Create stream hour-stream: ok')
else:
 print('Create stream hour-stream: error')
 print( response.text )
 # Create Daily Stream
query = {
 'stream-name': 'day-stream',
 'points-type': 'i' # 'i', 'f', or 's'
}
endpoint = '/networks/'+network_id+'/objects/day-object/streams/day-stream'
response = requests.request('PUT', base + endpoint, params=query, headers=header, timeout=120 )
resp = json.loads( response.text )
if resp['stream-code'] == 201:
 print('Create stream day-stream: ok')
else:
 print('Create stream day-stream: error')
 print( response.text )




###### SERVER communication functions ##########


def storeresults(results, t):
        
    
        #post entire results data structure to server for insertion into table, not plotting
        endpoint = '/networks/local/objects/result-object/streams/result-stream/points'
        print results
        jsonResults = json.dumps(results)
        query = {
            'points-value': jsonResults,
            'points-at': results['t']
        }             
        response = requests.request('POST', base + endpoint, params=query, headers=header, timeout=120 )
        resp = json.loads( response.text )
        print resp
        if resp['points-code'] == 200:
            print( 'Update result-stream points: ok')
        else:
            print( 'Update result-stream points: error')
            print( response.text )
            
            
            
        #Send point to daily highchartz stream for plotting    
        endpoint = '/networks/local/objects/day-object/streams/day-stream/points'
        print results
        query = {
            'points-value': results['Daily Stream'],
            'points-at': results['t']
        }             
        response = requests.request('POST', base + endpoint, params=query, headers=header, timeout=120 )
        resp = json.loads( response.text )
        print resp
        if resp['points-code'] == 200:
            print( 'Update day-stream points: ok')
        else:
            print( 'Update day-stream points: error')
            print( response.text )
         
            
            
        #Send point to hourly highchartz stream for plotting    
        endpoint = '/networks/local/objects/hour-object/streams/hour-stream/points'
        print results
        query = {
            'points-value': results['Hourly Stream'],
            'points-at': results['t']
        }
        response = requests.request('POST', base + endpoint, params=query, headers=header, timeout=120 )
        resp = json.loads( response.text )
        print resp
        if resp['points-code'] == 200:
            print( 'Update hour-stream points: ok')
        else:
            print( 'Update hour-stream points: error')
            print( response.text )    


#################### Revrieve Data from server######################
def loop(results):
    # Retrieve (GET) data from the server
    # Set url address.
    #base = 'http://127.0.0.1:5000'
    
    #get CO2 points
    try:
        endpoint = '/networks/local/objects/Arduino/streams/CO2/points'
        query = {}
        response = requests.request('GET', base + endpoint, params=query, headers=header, timeout=120 )
        resp = json.loads( response.text )
        if resp['points-code'] == 200:
            print( 'Receive CO2-stream points: ok')
            print resp['points'][0]['value'] 
            CO2 = resp['points'][0]['value'] 
            print results
            results['t'] = resp['points'][0]['at']            #stores timestamp in result structure
            print results['t']
        else:
            print( 'Receive CO2-stream points: error')
            print( response.text )
            CO2 = random.randint(0,2500)
            current = time.localtime()
            results['t'] = current.tm_sec
            print (results['t'])
            print("here CO2 loop")
            
        #get PM points  
        endpoint = '/networks/local/objects/Arduino/streams/PM/points'
        query = {}
        response = requests.request('GET', base + endpoint, params=query, headers=header, timeout=120 )
        resp = json.loads( response.text )
        if resp['points-code'] == 200:
            print( 'Recieve PM-stream points: ok')
            PM = resp['points'][0]['value']
        else:
            print( 'Recieve PM-stream points: error')
            print( response.text )
            PM = random.randint(0,50)
            
        #get RH points  
        endpoint = '/networks/local/objects/Arduino/streams/Humidity/points'
        query = {}
        response = requests.request('GET', base + endpoint, params=query, headers=header, timeout=120 )
        resp = json.loads( response.text )
        if resp['points-code'] == 200:
            print( 'Recieve RH-stream points: ok')
            RH = resp['points'][0]['value']
        else:
            print( 'Recieve RH-stream points: error')
            print( response.text )  
            RH = random.randint(0,100)
            
        #get VOC points  
        endpoint = '/networks/local/objects/Arduino/streams/VOC/points'
        query = {}
        response = requests.request('GET', base + endpoint, params=query, headers=header, timeout=120 )
        resp = json.loads( response.text )
        if resp['points-code'] == 200:
            print( 'Recieve VOC-stream points: ok')
            VOC = resp['points'][0]['value']
        else:
            print( 'Recieve VOC-stream points: error')
            print( response.text )
            VOC = random.randint(0,1200)
            
        #get temperature points  
        endpoint = '/networks/local/objects/Arduino/streams/Temperature/points'
        query = {}
        response = requests.request('GET', base + endpoint, params=query, headers=header, timeout=120 )
        resp = json.loads( response.text )
        if resp['points-code'] == 200:
            print( 'Recieve temp-stream points: ok')
            tempIN = resp['points'][0]['value']
        else:
            print( 'Recieve temp-stream points: error')
            print( response.text )
            tempIN = random.randint(8,30)
        
    except:
        print ("retreival failed")   
        
    time.sleep(1)    
    #data = [tempIN,PM,CO2,RH,VOC]   #store final data for later use
    
    
    ########### process data ##############
    try:

        #calculate average value for 5 inputs over lifetime of space monitoring
        #poorTimeX is a counter of "poor" rated measurements that is 
        #incremented within each rating if statement. MAY NEED TO COMPLICATE
        #THIS METRIC IF DIFFERENT TIME SCALES USED TO DEFINE POOR
        #All values stored in 1x5 lists of the order TPCRV
        
        
        #extract previous balues from results
        avg = results['Average Levels']           #Lifetime Average metrics of a space
        healthLevel = results['Health Level']     #Current rating for each metric
        aveHL = results['Average Health Level']   #average rating, used to determine if recommendations are displayed
        percentPoorTime = results['Percent Poor']   #Percent of readings with a poor rating
        readingNo = results['Reading Number'] + 1     #how many readings we have taken over space measurement lifetime
        dayStream = results['Daily Stream']       #single point to plot on daily average graph
        hourStream = results['Hourly Stream']      #single point to plot on hourly average graph
        t = results['t']                            #timestamp
        poorTime = results['Poor Time']       
        print('here result extraction for processing')
        
    ####### Aggregate Data
    
    
        #### Lifetime readings and summary
        
        #### 10 minute time scale readings + update averages
        #set outdoor temperature to fixed value of 16 C until weath data can be
        #pulled from weather API
        tempOUT = 16
        
        
        print('here before level checking') 
        # Temperature Check (C, Using adaptive comfort model)
        if tempIN < 10 or tempIN > 27:
            healthLevel[1] = 4
            poorTime[1] = poorTime[1] + 1
        elif tempIN < 22.6 +0.04*tempOUT - 6 or tempIN > 22.6 +0.04*tempOUT + 6:
            healthLevel[1] = 3
            poorTime[1] = poorTime[1] + 1
        elif tempIN < 22.6 +0.04*tempOUT - 4 or tempIN < 22.6 +0.04*tempOUT + 4:
            healthLevel[1] = 2
        else:
            healthLevel[1] = 1
            
        print('here in level checking')    
        # PM Check (micrograms per cubic meter)
        if PM > 45:
            healthLevel[2] = 4
            poorTime[2] = poorTime[2] + 1
        elif PM > 35:
            healthLevel[2] = 3
            poorTime[2] = poorTime[2] + 1            
        elif PM > 15:
            healthLevel[2] = 2
        else:
            healthLevel[2] = 1
            
        print("here before CO2 level checking")      
        # CO2 Check (ppm)
        if CO2 > 2000:
            healthLevel[3] = 4
            poorTime[3] = poorTime[3] + 1
        elif CO2 > 1000:
            healthLevel[3] = 3
            poorTime[3] = poorTime[3] + 1
        elif CO2 > 700:
            healthLevel[3] = 2            
        else:
            healthLevel[3] = 1
            
        print("here before RH level checking")      
        # RH Check (percent)
        if RH > 90 or RH < 10:
            healthLevel[4] = 4
            poorTime[4] = poorTime[4] + 1
        elif RH > 80 or RH < 20:
            healthLevel[4] = 3
            poorTime[4] = poorTime[4] + 1
        elif RH > 60 or RH < 40:
            healthLevel[4] = 2          
        else:
            healthLevel[4] = 1
            
            
        # VOC Check (micrograms per cubic meter)
        if VOC > 1000:
            healthLevel[5] = 4
            poorTime[5] = poorTime[5] + 1
        elif VOC > 500:
            healthLevel[5] = 2
            poorTime[5] = poorTime[5] + 1
        elif VOC > 300:
            healthLevel[5] = 2            
        else:
            healthLevel[5] = 1
            
        print("here HL calcs") 
        #find lifetime averages and percent of time with poor rating
        percentPoorTime[1] = poorTime[1]/readingNo
        percentPoorTime[2] = poorTime[2]/readingNo
        percentPoorTime[3] = poorTime[3]/readingNo
        percentPoorTime[4] = poorTime[4]/readingNo
        percentPoorTime[5] = poorTime[5]/readingNo
        
        avg[1] = (tempIN/readingNo)+avg[1]*(readingNo-1)/readingNo
        avg[2] = (PM/readingNo)+avg[2]*(readingNo-1)/readingNo
        avg[3] = (CO2/readingNo)+avg[3]*(readingNo-1)/readingNo
        avg[4] = (RH/readingNo)+avg[4]*(readingNo-1)/readingNo
        avg[5] = (VOC/readingNo)+avg[5]*(readingNo-1)/readingNo
        
        aveHL[1] = (healthLevel[1]/readingNo)+aveHL[1]*(readingNo-1)/readingNo
        aveHL[2] = (healthLevel[2]/readingNo)+aveHL[2]*(readingNo-1)/readingNo
        aveHL[3] = (healthLevel[3]/readingNo)+aveHL[3]*(readingNo-1)/readingNo
        aveHL[4] = (healthLevel[4]/readingNo)+aveHL[4]*(readingNo-1)/readingNo
        aveHL[5] = (healthLevel[5]/readingNo)+aveHL[5]*(readingNo-1)/readingNo


        print ("Temperature Rating = ", healthLevel[1])                
        print ("PM Health Rating = ", healthLevel[2])
        print ("CO2 Health Rating = ", healthLevel[3])
        print ("RH Health Rating = ", healthLevel[4])
        print ("VOC Health Rating = ", healthLevel[5])
        print ("Reading # = ", readingNo)
        print results['t']


        #run once at the start to initialize day and hour readings
        #if readingNo == 1:
        print("here initialize day hour") 
        #dayPt = 1
        #hourPt = 1
        dayStream =  [0,0,0,0,0]
        hourStream =  [0,0,0,0,0]

        #### 1 day time scale readings       
        
        #if readingNo % 144 == 0:
        #    for i in range(1,5):
        #        dayStream[i] = (data[i]/dayPt)+dayAvg[i]*(dayPt-1)/dayPt
        #        #dayPPTStream[i] =  dayPercentPoorTime/dayPt
        #        #dayHLStream[i] = (data[i]/dayPt)+dayAvg[i]*(dayPt-1)/dayPt
        #        dayAvg[i] = 1 
        #    dayPt = 1
        #    print("here day complete") 
        #else:
        #    for i in range(1,5):
        #        dayAvg[i] = (data[i]/dayPt)+dayAvg[i]*(dayPt-1)/dayPt
        #        #dayPercentPoorTime[i] =hourPercentPoorTime/dayPt
        #        #dayHL[i] = (data[i]/dayPt)+avgPM*(dayPt-1)/dayPt
        #
        #    dayPt = dayPt + 1
        #    print("here added day point") 
            
            
        #### 1 hour time scale readings
        
        #if readingNo % 6 == 0:   
        #    for i in range(1,5):
        #        hourStream[i] = (data[i]/hourPt)+hourAvg[i]*(hourPt-1)/hourPt
        #        #hourPPTStream[i] =  hourPercentPoorTime/hourPt
        #        #hourHLStream[i] = (data[i]/hourPt)+hourAvg[i]*(hourPt-1)/hourPt
        #        hourAvg[i] = 1
        #    hourPt = 1
        #    print("here hour complete") 
        #else:
        #    for i in range(1,5):
        #        hourAvg[i] = (data[i]/hourPt)+hourAvg[i]*(hourPt-1)/hourPt
        #        #hourPercentPoorTime[i] = hourPercentPoorTime/hourPt
        #        #hourHL[i] = (data[i]/hourPt)+hourAvg[i]*(hourPt-1)/hourPt
        #    hourPt = hourPt + 1
        #    print("here added hour point") 
            
        print dayStream
        print hourStream
        
        #print ("Total Light Exposure = "), totalLightExposure
        #print ("Average Light Exposure = "), avgLightExposure
        #print rec
        
        
        #output results of analysis for plotting and insertion into table. Assumes 10 min sample rate
        results = {'Average Levels': avg,            #Lifetime Average metrics of a space
                   'Health Level': healthLevel,      #Current rating for each metric
                   'Average Health Level': aveHL,    #average rating, used to determine if recommendations are displayed
                   'Poor Time': poorTime,
                   'Percent Poor':percentPoorTime,   #Percent of readings with a poor rating
                   'Reading Number':readingNo,       #how many readings we have taken over space measurement lifetime
                   'Daily Stream':dayStream,         #single point to plot on daily average graph
                   'Hourly Stream':hourStream,       #single point to plot on hourly average graph
                   't':t                             #timestamp
        }                       
                
                   #"Temp Health Level":TemphealthLevel,
                   #"PM Health Level":PMhealthLevel,
                   #"CO2 Health Level":CO2healthLevel,
                   #"RH Health Level":RHhealthLevel,
                   #"VOC Health Level":VOChealthLevel,
                   #"Average Temp":avgT,
                   #"Average PM":avgP,
                   #"Average CO2":avgC,
                   #"Average RH":avgR,
                   #"Average VOC":avgV,
                   #"Percent Unsatisfactory (Temp)":percentPoorTimeT,
                   #"Percent Unsatisfactory (PM)":percentPoorTimeP,
                   #"Percent Unsatisfactory (CO2)":percentPoorTimeC,
                   #"Percent Unsatisfactory (RH)":percentPoorTimeR,
                   #"Percent Unsatisfactory (VOC)":percentPoorTimeV,


        
        #collect data every 5 seconds
        time.sleep(5) 
        return results
    except:
        print("processing failed")    
    time.sleep(1) 
###### POST and structure functions ##########

# Run once at the start
def setup():
    try:
        print "Setup"
    except:
        print "Setup Error"




# Run continuously forever
# with a delay between calls
def delayed_loop():
    print "Delayed Loop"

#Run once at the end 
def close(): 
    try: 
        print "Close ListenAndProcess" 
        #ser.close() 
    except: 
        print "Close Error"
    


###### MAIN function ##########
  
def main():
    # Call setup function
    setup()
    # Set start time
    nextLoop = time.time()
    #readingNo = 0
    tLast=0
    results = {'Average Levels': [0,0,0,0,0,0],            #Lifetime Average metrics of a space
               'Health Level': [0,0,0,0,0,0],      #Current rating for each metric
               'Average Health Level': [0,0,0,0,0,0],    #average rating, used to determine if recommendations are displayed
               'Poor Time':[0,0,0,0,0,0],          #number of readings determined to be poor or worse
               'Percent Poor':[0,0,0,0,0,0],   #Percent of readings with a poor rating
               'Reading Number':0,       #how many readings we have taken over space measurement lifetime
               'Daily Stream':[0,0,0,0,0,0],         #single point to plot on daily average graph
               'Hourly Stream':[0,0,0,0,0,0],       #single point to plot on hourly average graph
               't':0
    } 
    #keyStrings = ["Average Levels","Health Level","Percent Poor","Reading Number","t"]
    #postStrings = {"T":[,,]}
    
    
    t=0
    time.sleep(1) 
    
    while(True):
        # Try loop() and delayed_loop()
        try:
            print('here1')
            time.sleep(0.5) 
            results = loop(results)
            #readingNo = results["Reading Number"]
            print("here outside loop")  
            t = results["t"]
            if t != tLast:
                print('here2')
                time.sleep(0.5) 
                print ("Sending Results: ") 
                print results
                storeresults (results, t)
                print('here3')
                tLast = t
                print tLast
            else:
                print("no results to store")
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
            time.sleep(1) 
    # Call close function
#    close()

# Run the program
#####NOTE: dont forget to restart the consoles if the server crashes.
#otherwise I'll get errors
main()
