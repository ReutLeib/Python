from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
from pprint import pprint


WinesURL = []
WinesURL.append("http://www.lcbo.com/lcbo/catalog/red-wine/11025")
WinesURL.append("http://www.lcbo.com/lcbo/catalog/white-wine/11003")
WinesURL.append("http://www.lcbo.com/lcbo/catalog/champagne/11026")
WinesURL.append("http://www.lcbo.com/lcbo/catalog/champagne/11016")
WinesURL.append("http://www.lcbo.com/lcbo/catalog/sparkling-wine/11018")
WinesURL.append("http://www.lcbo.com/lcbo/catalog/dessert-wine/11033")
WinesURL.append("http://www.lcbo.com/lcbo/catalog/icewine/11032")
data = []
dd = []
dt = []

# for WineURL in WinesURL:
Wine = urlopen("http://www.lcbo.com/lcbo/catalog/red-wine/11025")

# read html page
redSoup = BeautifulSoup(Wine.read(), "lxml")

# take all href from this page
redDiv = redSoup.findAll("div", {"class": "product-image"})
# print(redDiv)

# for each wine
for linkToPages in redDiv:
    wineName = linkToPages.find('a')['title']
    urlPage = "http://www.lcbo.com" + str(linkToPages.a['href'])
# print(urlPage)
    singlePage = urlopen(urlPage)
    singleSoup = BeautifulSoup(singlePage.read(), "lxml")
# priceVal = singleSoup.find("span", {"class": "price-value"})
    dlTag = singleSoup.find("dl", {})
    for dtTag in dlTag('dt')[1:]:
        dt.append(dtTag.contents[0])
        
    for ddTag in dlTag('dd')[1:]:
        dd.append(ddTag.contents[0])
    
# Merge 2 lists to one dictionary
    row = dict(zip(dt, dd))
    
    print(row)
    
    del dt[:]
    del dd[:]
    
    data.append(row)
    
#  @TODO:
#  1. Insert 'Wine name': wineName to row
#  2. Save the dictionary without the 'quots'
#  3. Make loop that scanning the pages:
#         PAGE1: productBeginIndex=0&beginIndex=0, PAGE2: productBeginIndex=12&beginIndex=12, PAGE3: productBeginIndex=24&beginIndex=24
#  4. Store the data in DATA1.json file
#  5. Interact with API to CROSS the with DATA1.json and make DATA2.json
#  6. in Location : Split the ',' delimiter to 'city' and 'country' 
#  7. in Sweetness Descriptor : get the current data from inner 'a' element
    
    
#     for i in row.keys():
#         print ('{} : {}\n'.format(i,row.get(i)))

#   with open('data.json', 'w') as outfile:
#   json.dump(data, outfile)