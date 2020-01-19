from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import random


driver = webdriver.Chrome(r'C:\Users\Xxmet\Downloads\SeleniumS\chromedriver')
driver.get('https://www.investopedia.com/financial-term-dictionary-4769738')

webs = []
page_digits = 7
page_num = random.randrange(4769351,4769377)
page_num = str(page_num)

url1 = ("https://www.investopedia.com/terms-beginning-with-a-") + page_num
driver.get(url1)

html = driver.find_element_by_id('dictionary-top300-list__list-content_1-0').get_attribute("innerHTML")[10:65]

webs.append(html)
webs_cleaned = ([s.strip('" id="diction') for s in webs])

print(webs_cleaned)

listToStr =' '.join([str(i) for i in webs_cleaned])
print(listToStr)
time.sleep(1)
driver.get(listToStr)
text = driver.find_element_by_id('article_1-0').get_attribute("innerText")
print(text)
driver.close()