from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options
import time
from bs4 import BeautifulSoup 

# url - might need replacing in ticket sale with specific URL
glasto_url = 'https://glastonbury.seetickets.com/'
# glasto_url = 'https://glastonbury.seetickets.com/queue/view?c=seeticketsuk&e=20241114glastocoach&ver=javascript-4.3.0&cver=68&man=Glastonbury%20Festival&enqueuetoken=eyJ0eXAiOiJRVDEiLCJlbmMiOiJBRVMyNTYiLCJpc3MiOjE3MzE2MDUyNTMxMDksInRpIjoiZmM0NWVmNjYtZDM4Yy00OWU2LWIzY2MtZTMxMDRlOTg4MmViIiwiYyI6InNlZXRpY2tldHN1ayIsImUiOiIyMDI0MTExNGdsYXN0b2NvYWNoIiwiaXAiOiI4Mi4xMzIuMjI1LjE2OCJ9.1XQvuKK-DgQJ-wUa15jpnw.B6WdNLTElK7wufZmCntN5cVZ4Oy8P66CZ5kB03eKxYM&t=https%3A%2F%2Fglastonbury.seetickets.com%2Fcontent%2Fextras&kupver=akamai-4.3.0'
is_queue_page = True

options = Options()
options.set_preference("general.useragent.override", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0")

driver = webdriver.Firefox(options=options)
driver.get(glasto_url)

while is_queue_page == True:
    
    time.sleep(1)
   
    try:
        # can change the wait time if this is too long. 
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        page_html = str(BeautifulSoup(driver.page_source, 'html.parser'))
        # if it doesn't stop then maybe additional is issue
        if "auto refresh" not in page_html.lower():
            is_queue_page = False
        else:
            driver.refresh()
            # maybe move this out of the else if having trouble with slow load


    except TimeoutException:
        print("Not loaded in time - Refresh")

    except Exception:
        print("Not loaded in time - Refresh")     
     

