import requests                                 #to process the request in a get method via the API
import json

with open('city.list.json') as f:                                            #open json file and read it
    data = json.load(f)                                                      #load its content to 'data'

f.close()

data2file = open("data2.json","w+")                                               #create a data2 file
    
obj_json = {
    'city': '',
    'Temperature': '',
    'Humidity': ''
}

#3 seasons
general_json = {
    'January':[
    ],
    'April':[
    ],
    'June':[
    ],
    'October':[
    ]    
}
cities = ['Washington', 'Chile', 'Bordeaux', 'Catalunya', 'Madrid']          #all cities that we have wines in - received from Data1 from crawler
dates = { 'January':'1515870589', 'April':'1523646589', 'June':'1528916989', 'October':'1542136189'}  #4 seasons in UNIX time

for city in cities:                                                          #for each city to search
    for dict in data:                                                        #search in the json data for it
        if dict['name'] == city:
            cityID = str(dict['id'])                                         #get the city ID
            cityLat = str(dict['coord']['lat'])                              #get the city Latitude
            cityLong = str(dict['coord']['lon'])                             #get the city Longtitude

    #https://api.darksky.net/forecast/[key]/[latitude],[longitude],[time] 
    for date in dates:                                                       #for each of the 4 seasons, get the temperature and humidity
        r = requests.get('https://api.darksky.net/forecast/a7896cfc9d0a3c6e26fecf1b8b560794/'+cityLat+','+cityLong+','+dates[date])            
        json_object = r.json()                                               #save it as a json object
        temp_c = ((json_object['currently']['temperature'] - 32) * (5/9))    #take the degress (supplied in fahrenheit) and convert them to celcious
        temp_h = json_object['daily']['data'][0]['humidity']                 #take the humidity
        
        obj_json = {'city':city, 'Temperature':temp_c, 'Humidity':temp_h}    #build the object
        general_json[date].append(obj_json)                                  #insert it to the general json object

#json_data = json.dumps(general_json)                                         #make sure the data is json like
print(general_json)                                                            #print it to the screen

json.dump(general_json, data2file)                                                  #write the data2 to the file
data2file.close()                                                                #close the data2 file
