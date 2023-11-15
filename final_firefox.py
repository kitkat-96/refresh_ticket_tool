from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
import time
from bs4 import BeautifulSoup 

# real url - might need replacing in ticket sale 
glasto_url = 'https://glastonbury.seetickets.com/content/extras'
is_queue_page = True

options = Options()
options.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0")

driver = webdriver.Firefox(options=options)
driver.get(glasto_url)

while is_queue_page == True:
    
    driver.refresh()
    time.sleep(1)
    
    try:
        # can change the wait time if this is too long. 
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        page_html = str(BeautifulSoup(driver.page_source, 'html.parser'))
        # if it doesn't stop then maybe postcode is issue
        if "postcode" in page_html.lower():
            is_queue_page = False

    except TimeoutException:
        print("Not loaded in time - Refresh")

    except Exception:
        print("Not loaded in time - Refresh")     
     

