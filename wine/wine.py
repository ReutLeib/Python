from bs4 import BeautifulSoup
from urllib.request import urlopen
import json
import requests

wine_urls = []
wine_category = {}
wine_pages = [5820, 2952, 324, 168, 420, 36, 60]
new_wine = []
data = []
dd = []
dt = []

# Getting the wine categories list
wine_list = urlopen("http://www.lcbo.com/content/lcbo/en/catalog/wine.html")
wine_list_soup = BeautifulSoup(wine_list.read(), 'html.parser')
wine_list_div = wine_list_soup.find("div", {"class": "nav"})
wine_list_div_li = wine_list_div.findAll("li", {})

# Parsing each wine category link
for wine in wine_list_div_li[0:7]:
    wine_urls.append('http://www.lcbo.com' + str(wine.a['href']))

print(wine_category)
print(wine_pages)
print(wine_urls)

# For loop to swipe between categories
j = 0
for wine in wine_urls[0:1]:              # Now Limited only for first category
    wine = wine.replace('/0/list', '')
    wine_category[j] = []
    i = 0
    # For loop to swipe between pages
    while i <= wine_pages[j]:
        # Cast int to string
        iStr = str(i)
        # Body parameters
        body = {
            'contentBeginIndex': 0,
            'productBeginIndex': iStr,
            'beginIndex': iStr,
            'orderBy': '',
            'pageView': '',
            'resultType': 'products',
            'orderByContent': '',
            'searchTerm': '',
            'facet': '',
            'storeId': 10151,
            'catalogId': 10001,
            'langId': -1,
            'fromPage': '',
            'loginError': '',
            'userId': -1002,
            'objectId': '',
            'requesttype': 'ajax'
        }
        # contains a characteristic string that allows the network protocol peers to identify the application type, operating system, software vendor or software version of the requesting software user agent
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
        }

        # Processing request
        response = requests.get(wine, params=body, headers=headers)
        print(f"Downaload from page: {response.url}")

        # new_wine = urlopen(pageURL).read()
        new_wine = response.content
        #  print(new_wine)
        wineSoup = BeautifulSoup(new_wine, 'html.parser')

       # print("PAGE NUMBER:" + iStr)

        # Getting all the wines of current page
        wineDiv = wineSoup.findAll("div", {"class": "product-image"})
        #print(wineDiv)

        # Parsing the data of each wine
        for linkToPages in wineDiv:

            # Opening the wine details page
            url_page = "http://www.lcbo.com" + str(linkToPages.a['href'])
            single_page = urlopen(url_page)
            single_soup = BeautifulSoup(single_page.read(), "html.parser")

            # Set name per wine
            wine_name = linkToPages.find('a')['title']
            dt.append("Wine Name")
            dd.append(wine_name)

            # Set price per wine
            wine_price = single_soup.find("span", {"class": "price-value"})
            dt.append("Price")
            dd.append(wine_price.get_text())

            # Getting the last <dl>
            dl_tag = single_soup.find_all('dl')[-1]

            # Parsing the <dt> details (key)
            for dt_tag in dl_tag('dt')[1:]:
                dt.append(dt_tag.get_text())

            # Parsing the <dd> details (value)
            for dd_tag in dl_tag('dd')[1:]:
                if dd_tag.a is not None:
                    dd.append(dd_tag.a.get_text())
                else:
                    dd.append(dd_tag.get_text())

            # Merge 2 lists into one dictionary
            row = dict(zip(dt, dd))

            # print(row)
            print("*")

            del dt[:]
            del dd[:]

            wine_category[j].append(row.copy())
            row.clear()

        # Next page
        i += 12

    # Number of pages for each wine category
    j += 1
    print(wine_category)

    with open('data.json', 'w') as fp:
        json.dump(wine_category, fp)
        
print('DATA1 Wine, Completed.')
