# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 00:00:19 2018

@author: Rodrigo
"""

import csv
import parameters
from parsel import Selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

# function to ensure all key data fields have a value
def validate_field(field):
    # if field is present pass if field:
    if field:
        pass
    # if field is not present print text else:
    else:
        field = 'No results'
    return field


# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('chromedriver.exe')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com')

# locate email form by_class_name
username = driver.find_element_by_class_name('login-email')

# send_keys() to simulate key strokes
username.send_keys(parameters.linkedin_username)

# sleep for 0.5 seconds
sleep(0.5)

# locate password form by_class_name
password = driver.find_element_by_class_name('login-password')

# send_keys() to simulate key strokes
password.send_keys(parameters.linkedin_password)
sleep(0.5)

# locate submit button by_xpath
sign_in_button = driver.find_element_by_xpath('//*[@type="submit"]')

# .click() to mimic button click
sign_in_button.click()
sleep(0.2)

# driver.get method() will navigate to a page given by the URL address
driver.get(parameters.linkedin_search)

i = 0
while True:
  # locate all elements
  elements = driver.find_elements_by_xpath('//*[contains(@class,"message-anywhere-button")]')
  if len(elements) > i:
      elements[i].click() # click on the i-th element in the list
      # locate message form by_class_name
      message = driver.find_element_by_xpath('//*[contains(@class,"msg-form__contenteditable")]')

      # send_message() to simulate key strokes
      message.send_keys(parameters.message)
      sleep(1)
      
      # locate submit button by_xpath
      send_button = driver.find_element_by_xpath('//*[contains(@class,"msg-form__send-button")]')

      # .click() to mimic button click
      send_button.click()
      sleep(1)
      
            # locate submit button by_xpath
      send_button = driver.find_element_by_xpath('//*[contains(@class,"msg-overlay-bubble-header__control js-msg-close")]')

      # .click() to mimic button click
      send_button.click()
      sleep(2)
                
      i += 1 # increment i
      sleep(1) # wait until list will be updated
      continue
  break 
j = 2
while True:
    try:
        driver.get(parameters.linkedin_search+'&page='+str(j))
        # locate all elements
        elem = driver.find_element_by_xpath('//*[contains(@class,"name actor-name")]')
   
        if elem.is_displayed():
            pass
        else: 
            break
        i = 0
        while True:
            # locate all elements
            elements = driver.find_elements_by_xpath('//*[contains(@class,"message-anywhere-button")]')
            if len(elements) > i:
                elements[i].click() # click on the i-th element in the list
                # locate message form by_class_name
                message = driver.find_element_by_xpath('//*[contains(@class,"msg-form__contenteditable")]')

                # send_message() to simulate key strokes
                message.send_keys(parameters.message)
                sleep(1)
      
                # locate submit button by_xpath
                send_button = driver.find_element_by_xpath('//*[contains(@class,"msg-form__send-button")]')

                # .click() to mimic button click
                send_button.click()
                sleep(1)
      
                # locate submit button by_xpath
                send_button = driver.find_element_by_xpath('//*[contains(@class,"msg-overlay-bubble-header__control js-msg-close")]')

                # .click() to mimic button click
                send_button.click()
                sleep(2)
                
                i += 1 # increment i
                sleep(1) # wait until list will be updated
                continue
            break
        j += 1 # increment j        
    except NoSuchElementException:
        break
    
# terminates the application
driver.quit()
       


