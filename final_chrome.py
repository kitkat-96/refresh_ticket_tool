from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from bs4 import BeautifulSoup 

# THIS LIKELY WILL NOT WORK ON MAC. HAVING ISSUES OF BROWSER QUITTING AFTER PAGE LOADS.

# real url - might need replacing
glasto_url = 'https://glastonbury.seetickets.com/content/extras'
is_queue_page = True
# will want to set headers 
headers = {}

driver = webdriver.Chrome()
driver.get(glasto_url)

while is_queue_page == True:
    
    driver.refresh()
    time.sleep(1)
    
    try:
        # can change the wait time if this is too long. 
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        page_html = str(BeautifulSoup(driver.page_source, 'html.parser'))
        # if it doesn't stop then maybe postcode issue
        if page_html.__contains__("postcode") or page_html.__contains__("Postcode"):
            is_queue_page = False

    # can change exception type?
    except TimeoutException:
        print("Not loaded in time - Refresh")

    # to just Exception? do we want both?
    except Exception:
        print("Not loaded in time - Refresh")     
     