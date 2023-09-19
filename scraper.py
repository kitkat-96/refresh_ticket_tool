from selenium import webdriver
import time
import random
from bs4 import BeautifulSoup 

glasto_url = 'file:///Users/katielovell/Documents/CodingProjects/glastonbury/own_bot/glasto_site.htm'
driver = webdriver.Firefox()
driver.get(glasto_url)

# write to file

# look at how to link beautiful soup and selenium!!
# /what to parse in instead of url
#  look at how the other bots did this for validation

soup = BeautifulSoup(glasto_url, 'html.parser')
# f.write(soup)
# https://www.codecademy.com/article/caupolicandiaz/web-scrape-with-selenium-and-beautiful-soup

# driver.get(random_generator)

# Refreshes the web page