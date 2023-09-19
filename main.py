from selenium import webdriver
import time
import random
from bs4 import BeautifulSoup 

# real url - might need replacing
# url = 'https://glastonbury.seetickets.com/content/extras'

# testing urls
glasto_url = 'file:///Users/katielovell/Documents/CodingProjects/glastonbury/own_bot/glasto_site.htm'
test_url = 'file:///Users/katielovell/Documents/CodingProjects/glastonbury/own_bot/test_site.htm'
site_options = [test_url, glasto_url]


# will want to set headers 
headers = {}

driver = webdriver.Firefox()

def gen_page ():
    page_choice = random.choices(site_options, weights=[0.9, 0.1])[0]
    return str(page_choice)

def refresh_page ():
        driver.get(gen_page())
        # driver.refresh()
        time.sleep(1)

count_refresh = 0
while count_refresh < 60:
    refresh_page()
    count_refresh += 1

# look at how to link beautiful soup and selenium
soup = BeautifulSoup(driver, 'html.parser')
print(soup)
# https://www.codecademy.com/article/caupolicandiaz/web-scrape-with-selenium-and-beautiful-soup

# driver.get(random_generator)

# Refreshes the web page
