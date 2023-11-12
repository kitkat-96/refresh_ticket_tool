from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from bs4 import BeautifulSoup 

# If glasto URL is different, replace this
glasto_url = 'https://glastonbury.seetickets.com/content/extras'
is_queue_page = True

driver = webdriver.Chrome('/usr/lib/chromium-browser/chromedriver')
driver.get(glasto_url)

while is_queue_page == True:
    driver.refresh()
    time.sleep(1)
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        page_html = str(BeautifulSoup(driver.page_source, 'html.parser'))
        
        if page_html.__contains__("postcode") or page_html.__contains__("Postcode"):
            is_queue_page = False

    except TimeoutException:
        print("Not loaded in time - Refresh")

    except Exception:
        print("Not loaded in time - Refresh")     
     

