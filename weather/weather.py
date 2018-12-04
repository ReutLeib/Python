import requests #to process the request in a get method via the API

cityID = '7302001'  #an example code for a specific city - there is a full city list in the API 
r = requests.get('http://api.openweathermap.org/data/2.5/weather?id='+cityID+'&appid=eee8747eb58c05ad3f545d00d778fd0a') #get the response using the city code
json_object = r.json()  #save it as a json object
temp_c = (float(json_object['main']['temp']) -273.15) #take the degress (supplied in kalvin) and convert them to celcious
print(temp_c) #print them to the screen (just to check)
