from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import math
import copy

class Message():
    def __init__(self, user, message):
        self.user = user
        self.message = message
    def __eq__(self, other):
        return self.user == other.user and self.message == other.message

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=data/Training")
driver = webdriver.Chrome(chrome_options=options)
driver.get('http://www.square-bear.co.uk/mitsuku/nfchat.htm')

while True:
    try:

        # Switch tabs and get Response
        driver.switch_to_window(driver.window_handles[1])
        textField = driver.find_elements_by_tag_name("input")
        print(textField.size())
        for i in range(textField.size()):

        print(textField.text)

        input()

        for querry in replyQueue:
            textField.sendKeys(querry)
            textField.submit() 

        input()
        
    except Exception as e:
        print(str(e))



