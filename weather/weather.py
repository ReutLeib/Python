import requests                                 #to process the request in a get method via the API
import json
from pprint import pprint

with open('city.list.json') as f:                    #open json file and read it
    data = json.load(f)

cities = ['Washington', 'Chile', 'Bordeaux', 'Catalunya', 'Madrid']
dates = { 'January':'1515870589', 'April':'1523646589', 'June':'1528916989', 'October':'1542136189'}
for city in cities:                             #for each city to search
    for dict in data:                           #search in the json data for it, and return the cityID
        if dict['name'] == city:
            cityID = str(dict['id'])
            cityLat = str(dict['coord']['lat'])
            cityLong = str(dict['coord']['lon'])

    #https://api.darksky.net/forecast/[key]/[latitude],[longitude],[time] 
    #for dateKey, dateVal in dates.iteritems():
    for date in dates:
        r = requests.get('https://api.darksky.net/forecast/a7896cfc9d0a3c6e26fecf1b8b560794/'+cityLat+','+cityLong+','+dates[date])            
        json_object = r.json()                                               #save it as a json object
        temp_c = ((json_object['currently']['temperature'] - 32) * (5/9))        #take the degress (supplied in fahrenheit) and convert them to celcious
        temp_h = json_object['daily']['data'][0]['humidity']
        print(city)
        print("Month: "+date)
        print("Temperature: "+str(temp_c))
        print("Humidity: "+str(temp_h))
        print('********************')
