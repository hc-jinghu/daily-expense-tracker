import os
import gspread
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver = "/chromedriver"
option = webdriver.ChromeOptions()
option.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
s = Service(chromedriver)
driver = webdriver.Chrome(service=s, options=option)
wait = WebDriverWait(driver, 20)

load_dotenv()
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

driver.get("https://secure.royalbank.com/statics/login-service-ui/index#/full/signin?LANGUAGE=ENGLISH")
wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="userName"]')))
driver.find_element(By.XPATH, '//*[@id="userName"]').send_keys(USERNAME)
driver.find_element(By.XPATH, '//a[@id="signinNext"]').click()
driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(PASSWORD)
driver.find_element(By.XPATH, '//*[@id="signinNext"]').click()
#TODO: need to program a wait so it waits for 2 step verification
#TODO: goes into visa card section and scrape authorized transactions
#TODO: compare transactions, not sure if this should be in here
'''
if same amount
    if same date, don't record cuz it's possibly a pending transaction
else record everything
'''

driver.quit()