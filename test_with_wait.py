from selenium import webdriver
import time
import random
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait 

# real url - might need replacing
# url = 'https://glastonbury.seetickets.com/content/extras'

# testing urls
glasto_url = 'file:///Users/katielovell/Documents/CodingProjects/glastonbury/own_bot/glasto_site.htm'
queue_url = 'file:///Users/katielovell/Documents/CodingProjects/glastonbury/own_bot/glasto_queue.htm'
site_options = [queue_url, glasto_url]
is_queue_page = True


# will want to set headers 
headers = {}

driver = webdriver.Firefox()

#  throws up test site
def gen_page ():
    page_choice = random.choices(site_options, weights=[0.92, 0.08])[0]
    return str(page_choice)

def refresh_page ():
        driver.get(gen_page())
        # driver.refresh()
        time.sleep(1)

while is_queue_page == True: # this will change to the while false or something 
    
    try:
         WebDriverWait()
         
    refresh_page()
    page_html = str(BeautifulSoup(driver.page_source, 'html.parser'))
    # if postcode appears on queue page this will not work. 
    # If postcode does not appear on main page this will not work
    if page_html.__contains__("postcode") or page_html.__contains__("Postcode"):
        print("banging")
        is_queue_page = False


# look at how to link beautiful soup and selenium
# soup = BeautifulSoup(driver, 'html.parser')
# print(soup)
# # https://www.codecademy.com/article/caupolicandiaz/web-scrape-with-selenium-and-beautiful-soup

# driver.get(random_generator)

# Refreshes the web page
