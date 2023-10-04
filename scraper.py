from selenium import webdriver
import time
import random
from bs4 import BeautifulSoup 

glasto_url = 'file:///Users/katielovell/Documents/CodingProjects/glastonbury/own_bot/glasto_site.htm'
queue_url = 'file:///Users/katielovell/Documents/CodingProjects/glastonbury/own_bot/glasto_queue.htm'

driver = webdriver.Firefox()
driver.get(queue_url)

# write to file

# look at how to link beautiful soup and selenium!!
# /what to parse in instead of url
#  look at how the other bots did this for validation

soup = BeautifulSoup(driver.page_source, 'html.parser')
# print(soup)

file = open("soup_text.txt", "w")
file.write(str(soup))
file.close()

if str(soup).__contains__("postcode") or str(soup).__contains__("Postcode"):
    print("not banging")

# https://www.codecademy.com/article/caupolicandiaz/web-scrape-with-selenium-and-beautiful-soup

# driver.get(random_generator)

# Refreshes the web page