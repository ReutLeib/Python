import requests

cityID = '7302001'
r = requests.get('http://api.openweathermap.org/data/2.5/weather?id='+cityID+'&appid=eee8747eb58c05ad3f545d00d778fd0a')
json_object = r.json()
temp_c = (float(json_object['main']['temp']) -273.15)
print(temp_c)