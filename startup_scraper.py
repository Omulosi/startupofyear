import os
from lxml.html import fromstring
import os
import pandas as pd
from throttle import Throttle

SLEEP_TIME = 2
CURRENT_DIR = os.getcwd()
throttle = Throttle(3)

# name
STARTUP_NAME_XPATH = './/div[contains(@class, "s-item-title")]//div[contains(@class, "s-component-content")]'
STARTUP_NAME_XPATH_B = './/div[contains(@class, "s-item-title")]//a/text()'
STARTUP_NAME_XPATH_C = './/div[contains(@class, "s-item-title")]//u/text()'

# link
STARTUP_LINK_XPATH = './/div[contains(@class, "s-item-title")]//a/@href'

# location
STARTUP_LOCATION_XPATH = './/div[contains(@class, "s-item-subtitle")]//div[contains(@class, "s-component-content")]'


def scraper(url, html):
    STARTUPS = []
    
    tree = fromstring(html)
    # List of elements containing startup items
    startup_items = tree.xpath('//div[contains(@class, "s-repeatable")]//div[contains(@class, "s-repeatable-item")]')
    
    for index, item in enumerate(startup_items):
        name = item.xpath(STARTUP_NAME_XPATH)
        if not name:
            continue
        
        name = name[0].text_content()
        try:
            name, location = name.split('|')
            name = name.strip()
            location = location.strip()
        except (IndexError, ValueError):
            location = None
            
        link = item.xpath(STARTUP_LINK_XPATH) or None
        if link:
            link = link[0]
        
        if not location:
            location = item.xpath(STARTUP_LOCATION_XPATH)
            if location:
                location = location[0].text_content().strip()       
        
        STARTUPS.append((name, location, link))
            
        print(f"============ {index} ==============")
        print(f"Name ===> {name}")
        print(f"Location =======> {location}")
        print(f"Link  ===> {link}")
        
    df  = pd.DataFrame(STARTUPS, columns=['Name', 'Location', 'Link'], index=None)
    df.to_csv('data.csv')