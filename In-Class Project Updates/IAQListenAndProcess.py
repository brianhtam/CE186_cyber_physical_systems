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
sys.path.append(r'C:\Python27\Lib\site-packages')
import serial

sys.path.append(r'C:\Python27\Lib')
import json

sys.path.append(r'C:\Python27\Lib\site-packages\pip\_vendor')
import requests 

import time
import datetime



delay = 5 # Delay in seconds

base = 'http://127.0.0.1:5000'
network_id = 'local'
header = {}




###### SERVER communication functions ##########


def storeresults(results):
        
    
        #post entire results data structure to server for insertion into table, not plotting
        endpoint = '/networks/local/objects/result-object/streams/result-stream/points'
        print results
        query = {
            'points-value': results,
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
            'points-value': results["Daily Stream"],
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
            'points-value': results["Hourly Stream"],
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
def loop(timeL,tLE,tT,rN,resultsLast):
    # Retrieve (GET) data from the server
    # Set url address.
    #base = 'http://127.0.0.1:5000'
    
    #get CO2 points
    try:
            endpoint = '/networks/local/objects/CO2-object/streams/CO2-stream/points'
            query = {}
            response = requests.request('GET', base + endpoint, params=query, headers=header, timeout=120 )
            resp = json.loads( response.text )
            if resp['points-code'] == 200:
                print( 'Receive CO2-stream points: ok')
                print resp['points'][0]['value'] 
                CO2IN = resp['points'][0]['value'] 
                t= resp['points'][0]['at']
            else:
                print( 'Receive CO2-stream points: error')
                print( response.text )
                t = 
            
            
        #get PM points  
        endpoint = '/networks/local/objects/PM-object/streams/PM-stream/points'
        query = {}
        response = requests.request('GET', base + endpoint, params=query, headers=header, timeout=120 )
        resp = json.loads( response.text )
        if resp['points-code'] == 200:
            print( 'Recieve PM-stream points: ok')
            PMIN = resp['points'][0]['value']
        else:
            print( 'Recieve PM-stream points: error')
            print( response.text )     
            
        #get RH points  
        endpoint = '/networks/local/objects/RH-object/streams/RH-stream/points'
        query = {}
        response = requests.request('GET', base + endpoint, params=query, headers=header, timeout=120 )
        resp = json.loads( response.text )
        if resp['points-code'] == 200:
            print( 'Recieve RH-stream points: ok')
            RHIN = resp['points'][0]['value']
        else:
            print( 'Recieve RH-stream points: error')
            print( response.text )  
            
        #get VOC points  
        endpoint = '/networks/local/objects/VOC-object/streams/VOC-stream/points'
        query = {}
        response = requests.request('GET', base + endpoint, params=query, headers=header, timeout=120 )
        resp = json.loads( response.text )
        if resp['points-code'] == 200:
            print( 'Recieve VOC-stream points: ok')
            VOCIN = resp['points'][0]['value']
        else:
            print( 'Recieve VOC-stream points: error')
            print( response.text )  
            
        #get temperature points  
        endpoint = '/networks/local/objects/temp-object/streams/temp-stream/points'
        query = {}
        response = requests.request('GET', base + endpoint, params=query, headers=header, timeout=120 )
        resp = json.loads( response.text )
        if resp['points-code'] == 200:
            print( 'Recieve temp-stream points: ok')
            tempIN = resp['points'][0]['value']
        else:
            print( 'Recieve temp-stream points: error')
            print( response.text )  
        
    except:
        print ("retreival failed")    
    time.sleep(1) 
    
    
    
    ########### process data ##############
    try:
        #process the results. total exposure = sum of light levels retrieved
        readingNo = rN + 1
        #calculate average value for 5 inputs over lifetime of space monitoring
        #poorTimeX is a counter of "poor" rated measurements that is 
        #incremented within each rating if statement. MAY NEED TO COMPLICATE
        #THIS METRIC IF DIFFERENT TIME SCALES USED TO DEFINE POOR
        #All values stored in 1x5 lists of the order TPCRV
        percentPoorTimeT = poorTimeT/readingNo
        percentPoorTimeP = poorTimeP/readingNo
        percentPoorTimeC = poorTimeC/readingNo
        percentPoorTimeR = poorTimeR/readingNo
        percentPoorTimeV = poorTimeV/readingNo
        
        avgTemp = (TempIN/readingNo)+avgTemp*(readingNo-1)/readingNo
        avgPM = (PM/readingNo)+avgPM*(readingNo-1)/readingNo
        avgCO2 = (CO2/readingNo)+avgCO2*(readingNo-1)/readingNo
        avgRH = (RH/readingNo)+avgRH*(readingNo-1)/readingNo
        avgVOC = (VOC/readingNo)+avgVOC*(readingNo-1)/readingNo
        
        
    ####### Aggregate Data
    
    
        #### Lifetime readings and summary
        
        #### 1 day time scale readings
        if readingNo % 144 == 0:
            dayStream = (PM/readingNo)+avgPM*(readingNo-1)/readingNo
            dayPPTStream =  poorTime/dayPt
            dayHLStream = (PM/readingNo)+avgPM*(readingNo-1)/readingNo
            dayPt = 0
        else
            dayAvg = 
            dayPercentPoorTime
            dayHL=
            dayPt = dayPt +1
        #### 1 hour time scale readings
        if readingNo % 6 == 0        
        
        
        
        #### 10 minute time scale readings + update averages
        
        # Temperature Check (Using adaptive comfort model)
        if tempIN < 22.6 +0.04*tempOUT - 6 or tempIN > 22.6 +0.04*tempOUT + 6:
            healthLevel = 3
            poorTimeT = poorTimeT + 1
            rec = "Thermal comfort estimate: Poor"
        elif tempIN < 22.6 +0.04*tempOUT - 5 or tempIN < 22.6 +0.04*tempOUT + 5:
            healthLevel = 2
            rec = "Thermal comfort estimate: Fair"
        else:
            healthLevel = 1
            rec = "Thermal comfort estimate: Good"
            
            
        # PM Check
        if PM <= 25:
            healthLevel = 1
            poorTimeP = poorTimeP + 1
            rec = "Healthy conditions, no recommendation"
        elif tempIN > 25 & tempIN <= 27:
            healthLevel = 2
            rec = "Temperature is high, consider turning down the thermostat"
        else:
            healthLevel = 3
            rec = "Heat stroke imminent, activating fan"
            
            
        # CO2 Check
        if CO2 <= 25:
            healthLevel = 1
            poorTimeC = poorTimeC + 1
            rec = "Healthy conditions, no recommendation"
        elif tempIN > 25 & tempIN <= 27:
            healthLevel = 2
            rec = "Temperature is high, consider turning down the thermostat"
        else:
            healthLevel = 3
            rec = "Heat stroke imminent, activating fan"
            
            
        # RH Check
        if RH <= 25:
            healthLevel = 1
            poorTimeR = poorTimeR + 1
            rec = "Healthy conditions, no recommendation"
        elif tempIN > 25 & tempIN <= 27:
            healthLevel = 2
            rec = "Temperature is high, consider turning down the thermostat"
        else:
            healthLevel = 3
            rec = "Heat stroke imminent, activating fan"
            
            
        # VOC Check
        if VOC <= 25:
            healthLevel = 1
            poorTimeV = poorTimeV + 1
            rec = "Healthy conditions, no recommendation"
        elif tempIN > 25 & tempIN <= 27:
            healthLevel = 2
            rec = "Temperature is high, consider turning down the thermostat"
        else:
            healthLevel = 3
            rec = "Heat stroke imminent, activating fan"
                
        print ("PM Health Level = "), PMhealthLevel
        print ("CO2 Health Level = "), CO2healthLevel
        print ("RH Health Level = "), RHhealthLevel
        print ("VOC Health Level = "), VOChealthLevel
        print ("Temperature Level= "), TemphealthLevel
        
        print ("Reading # = "), readingNo
        #print ("Total Light Exposure = "), totalLightExposure
        #print ("Average Light Exposure = "), avgLightExposure
        print rec
        
        
        #output results of analysis for plotting and insertion into table. Assumes 10 min sample rate
        results = {"Average Levels": avg,           #Lifetime Average metrics of a space
                   "Health Level": healthLevel,     #Current rating for each metric
                   "Average Health Level": aveHL    #average rating, used to determine if recommendations are displayed
                   "Percent Poor":percentPoorTime,  #Percent of readings with a poor rating
                   "Reading Number":readingNo       #how many readings we have taken over space measurement lifetime
                   "Daily Stream":dayStream         #single point to plot on daily average graph
                   "Hourly Stream":hourStream       #single point to plot on hourly average graph
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
    readingNo = 0
    #tLast=0
    results = {"Average Levels": 0,
               "Health Level": 0,
               "Percent Poor":0,
               #"Day stream":0, #Bonus
               #"Hour stream":0,  #Bonus
               "Reading Number":0,       
               "t":0 
    }
    keyStrings = ["Average Levels","Health Level","Percent Poor","Reading Number","t"]
    postStrings = {"T":[,,]}
    
    
    t=0
    time.sleep(1) 
    
    while(True):
        # Try loop() and delayed_loop()
        try:
            results = loop(results)
            #readingNo = results["Reading Number"]
            t = results["t"]
            if t != tLast:
                print ("Sending Results: ") 
                print results
                storeresults (results, t, postStrings)
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
    # Call close function
#    close()

# Run the program
#####NOTE: dont forget to restart the consoles if the server crashes.
#otherwise I'll get errors
main()
