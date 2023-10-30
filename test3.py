from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import time
from timeit import default_timer as timer
from bs4 import BeautifulSoup 

# real url - might need replacing
glasto_url = 'https://glastonbury.seetickets.com/content/extras'
is_queue_page = True


# will want to set headers 
headers = {}

driver = webdriver.Firefox()

driver.get(glasto_url)
while is_queue_page == True: # this will change to the while false or something 
    # timeout not working
    driver.refresh()
    start = timer()
    try:
        WebDriverWait(driver, 2, 0.001).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
        end = timer()
        print(f"loaded in {(end-start)}")
        page_html = str(BeautifulSoup(driver.page_source, 'html.parser'))
        # if postcode appears on queue page this will not work. 
        # If postcode does not appear on main page this will not work
        if page_html.__contains__("postcode") or page_html.__contains__("Postcode"):
            is_queue_page = False
        time.sleep(1)

    except TimeoutException:
        print("exception")


# look at how to link beautiful soup and selenium
# soup = BeautifulSoup(driver, 'html.parser')
# print(soup)
# # https://www.codecademy.com/article/caupolicandiaz/web-scrape-with-selenium-and-beautiful-soup

# driver.get(random_generator)

# Refreshes the web page
