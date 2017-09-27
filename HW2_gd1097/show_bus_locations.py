
# coding: utf-8


import pylab as pl
import sys
import os
import json
import numpy as np
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

def getData(url):
    response = urllib.urlopen(url)
    data = response.read().decode("utf-8")
    data = json.loads(data)
    return data

key=sys.argv[1]
busNumber=sys.argv[2]
    

url='http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s'%(key,busNumber)

data=getData (url)


number=np.size(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])


print('Bus Line: ', busNumber)
print('Number of Active Busses: ', number)

for k in range(0,number):
    Lat = getData (url)['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][k]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    Long =getData (url)['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][k]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print ('Bus', k ,'is at latitude', Lat ,'and longitude', Long)




