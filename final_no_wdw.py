from selenium import webdriver
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

# did we need a web driver wait
    page_html = str(BeautifulSoup(driver.page_source, 'html.parser'))
    # if it doesn't stop then maybe postcode issue
    if page_html.__contains__("postcode") or page_html.__contains__("Postcode"):
        is_queue_page = False
     

