from selenium import webdriver
import time
import random
from bs4 import BeautifulSoup 

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
    page_choice = random.choices(site_options, weights=[0.9, 0.1])[0]
    return str(page_choice)

def refresh_page ():
        driver.get(gen_page())
        # driver.refresh()
        time.sleep(1)

while is_queue_page == True: # this will change to the while false or something 
    refresh_page()
    page_html = str(BeautifulSoup(driver.page_source, 'html.parser'))
    # if postcode appears on queue page this will not work. 
    # If postcode does not appear on main page this will not work
    if page_html.__contains__("postcode") or page_html.__contains__("Postcode"):
        is_queue_page = False
