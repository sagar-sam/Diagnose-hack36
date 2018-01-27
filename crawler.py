import selenium, time
import urllib2
import json
import os
import sys
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get('https://www.google.co.in/')
wait=WebDriverWait(browser,50)

search = wait.until(ec.presence_of_element_located((By.XPATH,"//*[@id='lst-ib']")))
search.send_keys('liver disease')

#time.sleep(1)

press_key = wait.until(ec.presence_of_element_located((By.XPATH,"/html/body/div/div[3]/form/div[2]/div[3]/center/input[1]")))
press_key.click()

images = wait.until(ec.presence_of_element_located((By.XPATH,"//*[@id='hdtb-msb-vis']/div[2]/a")))
images.click()

images = browser.find_elements_by_tag_name('img')

i=0

for image in images:
	print(image.get_attribute('src'))
	img_url = json.loads(image.get_attribute('innerHTML'))["ou"]
	img_type = json.loads(image.get_attribute('innerHTML'))["ity"]
	print img_url
	req = urllib2.Request(img_url)
	raw_img = urllib2.urlopen(req).read()
	f = open(str(i)+".jpg","wb")
	f.write(raw_img)
	f.close()
#	urllib.urlretrieve(image.get_attribute('src'),str(i)+".png")
#	i=i+1

time.sleep(5)

browser.close()