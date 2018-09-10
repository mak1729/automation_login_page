#!/usr/bin/env python

from selenium import webdriver
from   selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome()
browser.get('https://www.facebook.com/')


username = browser.find_element_by_id("email" )
password = browser.find_element_by_id( "pass" )
submit   = browser.find_element_by_id( "u_0_2"   )
  

username.send_keys( "mak1729" )
password.send_keys( "i@mayank9154" )
  

submit.click()
  

wait = WebDriverWait( browser, 5 )
  
try:
	page_loaded = wait.until_not(lambda browser: browser.current_url == login_page)
except TimeoutException:
	self.fail( "Loading timeout expired" )
self.assertEqual(
	browser.current_url,
	correct_page,
	msg = "Successful Login"
)