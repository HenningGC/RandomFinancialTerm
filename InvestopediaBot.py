from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import random


driver = webdriver.Chrome()
driver.get('https://www.investopedia.com/financial-term-dictionary-4769738')

webs = []
page_digits = 7
page_num = random.randrange(4769351,4769377)
page_num = str(page_num)
term_num = random.randrange(1,280)
term_num = str(term_num)

url1 = ("https://www.investopedia.com/terms-beginning-with-a-") + page_num
driver.get(url1)

elems = driver.find_element_by_id("dictionary-top300-list__list_1-0-" + term_num).get_attribute("href")
time.sleep(0.5)
driver.get(elems)
text = driver.find_element_by_id('article_1-0').get_attribute("innerText")
print(text)
driver.close()
input('Press ENTER to exit')
