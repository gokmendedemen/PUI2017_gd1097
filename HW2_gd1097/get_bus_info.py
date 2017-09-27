
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
output_csv=sys.argv[3]
fout = open(output_csv, "w")
fout.write('Latitude,Longitude,Stop Name,Stop Status\n')

url='http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s'%(key,busNumber)

data=getData (url)


number=np.size(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])


print('Bus Line: ', busNumber)
print('Number of Active Busses: ', number)

for k in range(0,number):
    Lat = getData (url)['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][k]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    Long =getData (url)['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][k]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    print ('Bus', k ,'is at latitude', Lat ,'and longitude', Long)
    if np.size(getData(url)['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][k]['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']) == 0:
        StopName = 'N/A'
    else:
        StopName = getData(url)['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][k]['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
    if np.size(getData(url)['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][k]['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']) == 0:
       StopStatus = 'N/A'
    else:
       StopStatus = getData(url)['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][k]['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']


    fout.write('{},{},{},{}\n'.format(Lat,Long,StopName,StopStatus))

