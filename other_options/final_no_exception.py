from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup 

# real url - might need replacing
glasto_url = 'https://glastonbury.seetickets.com/content/extras'
is_queue_page = True
# will want to set headers 
headers = {}

driver = webdriver.Firefox()
driver.get(glasto_url)

while is_queue_page == True:
    
    driver.refresh()
    time.sleep(1)
    # can change the wait time if this is too long
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    page_html = str(BeautifulSoup(driver.page_source, 'html.parser'))
    # if it doesn't stop then maybe postcode issue
    if "deposit" in page_html.lower():
        is_queue_page = False
     

