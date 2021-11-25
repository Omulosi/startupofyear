from startup_scraper import scraper
from link_crawler import link_crawler

START_URL = 'https://www.startupofyear.com/alumni'

if __name__ == '__main__':
    # Todo: Update link to follow
    follow = r'/map/' 
    link_crawler(START_URL, link_regex=None, scraper_callback=scraper)
    
    
    

# import scrapers
# import csv
# import pandas as pd
# from cache import Cache

# STARTUPS_OF_YEAR = []

# for row in records.itertuples(index=False):
#     name, institution = getattr(row, 'name'), getattr(row, 'company')

#     if isinstance(institution, str) and 'princeton' in institution.lower():
#         # extract email
#         email = scrapers.princeton_scraper(parse_name(name))
#         if email is None: continue
#         EMAILS.append((name, institution, email))


# #print(EMAILS)

# df  = pd.DataFrame(STARTUPS_OF_YEAR, columns=['name', 'location', 'URL'])
# df.to_csv('data.csv')