
# WEB SCRAPPER #

from bs4 import BeautifulSoup        # pip install beautifulsoup4 #       
import requests                      # pip install requests #
import pandas as pd                  # pip install pandas # 

page = requsts.get('url')                          # User can enter the url #
soup = BeautifulSoup(page.content,'html.parser')   # Extract the html contents #
print(soup)                                        # Prints out the Extracted html contents# 

# Url used in this pgm is 'https://forecast.weather.gov/MapClick.php?lat=61.21753000000007&lon=-149.85824999999997#.X4QzCsIzbIU' #
# Rest of the code is based on the html contents of above webpage #

week = soup.find(id='')
print(week)

items = week.find_all(class_= '')
print(items[])

print(item[].find(class_='').get_text())

period_name = (item.find(class_='').get_text() for item in items)
short_description = (item.find(class_='').get_text() for item in items)
temparature= (item.find(class_='').get_text() for item in items)

print(period_names)
print(short_description)
print(temparature)

weather_stuff = pd.DataFrames({                # Represents the Extracted Info in dictionary and converts it to csv format #
 'Period': period_name,               
 'Short Description': short_description,
 'Temparature': temparature
}) 
print(weather_stuff)                           # User can also print the info available in Excel Sheets #
