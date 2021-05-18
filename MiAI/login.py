from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(executable_path='E:\Documents\Python\logincrawl\chromedriver')

browser.get('https://facebook.com')
sleep(3)

txtUser = browser.find_element_by_id('email')
txtUser.send_keys('0965584120')
sleep(1)

txtPasswork=browser.find_element_by_id('pass')
txtPasswork.send_keys('024120195hoang')
sleep(1)
txtPasswork.send_keys(Keys.ENTER)
sleep(1)
approval = browser.find_element_by_id('approvals_code')
approval.send_keys('123456')

