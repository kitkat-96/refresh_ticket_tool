from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
import random
from bs4 import BeautifulSoup 


# testing urls - this path will need to be changed for each computer 
glasto_url = 'file:///Users/katielovell/Documents/CodingProjects/glastonbury/own_bot/test_code/glasto_site.htm'
queue_url = 'file:///Users/katielovell/Documents/CodingProjects/glastonbury/own_bot/test_code/glasto_queue.htm'
site_options = [queue_url, glasto_url]
is_queue_page = True

options = Options()
options.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 14.1; rv:109.0) Gecko/20100101 Firefox/119.0")

driver = webdriver.Firefox(options=options)

#  throws up test site
def gen_page ():
    page_choice = random.choices(site_options, weights=[0.9, 0.1])[0]
    return str(page_choice)

def refresh_page ():
        driver.get(gen_page())
        time.sleep(1)

while is_queue_page == True: # this will change to the while false or something 
    refresh_page()
    WebDriverWait(driver, 1).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    page_html = str(BeautifulSoup(driver.page_source, 'html.parser'))
    # if postcode appears on queue page this will not work. 
    # If postcode does not appear on main page this will not work
    if "postcode" in page_html.lower():
        is_queue_page = False
