############################# THIS FILE NOT WORKING

from instapy import InstaPy

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Firefox()
browser.get('https://www.instagram.com/')

cookies_button = browser.find_element(By.XPATH, '//button[text()="Accept All"]')
cookies_button.click()

#h2 = browser.find_element(By.XPATH, '//button[text()="Accept Cookies"]')
#h2.click()


InstaPy(username= "convolvulus3", password="waterballtapestarwars1234").login()




