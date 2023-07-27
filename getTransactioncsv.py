import os
import time
import random
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

waitTime = random.uniform(3.3, 6.5)

load_dotenv()
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")
ACC = os.environ.get("RBCIONPLUS")
TRANSACTIONCSVPATH = os.environ.get("TRANSACTIONCSVPATH")

prefs = {"download.default_directory" : TRANSACTIONCSVPATH}

chromedriver = "/chromedriver"
option = webdriver.ChromeOptions()
option.add_experimental_option("prefs", prefs)
option.add_experimental_option("detach", True)
option.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
s = Service(chromedriver)
driver = webdriver.Chrome(service=s, options=option)
wait = WebDriverWait(driver, 20)

def login(driver):
    # Adjust this section if needed
    driver.get("https://secure.royalbank.com/statics/login-service-ui/index#/full/signin?LANGUAGE=ENGLISH")
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="userName"]')))
    driver.find_element(By.XPATH, '//*[@id="userName"]').send_keys(USERNAME)
    driver.find_element(By.XPATH, '//a[@id="signinNext"]').click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(PASSWORD)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="signinNext"]').click()

def downloadcsv(driver):
    # goes into visa card section
    driver.get(ACC)
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.XPATH, '//a[@id="main"]/rbc-details-layout-widget/rbc-frame/article/section/div[3]/rbc-transaction-table-container/rbc-cc-transactions-container/div[2]/rbc-cc-posted-transaction-header/div/div[2]/a')))
    driver.find_element(By.XPATH, '//a[@id="main"]/rbc-details-layout-widget/rbc-frame/article/section/div[3]/rbc-transaction-table-container/rbc-cc-transactions-container/div[2]/rbc-cc-posted-transaction-header/div/div[2]/a').click()
    time.sleep(waitTime)
    # download csv
    wait.until(EC.presence_of_element_located((By.XPATH, '//input[@id="Excel"]')))
    driver.find_element(By.XPATH, '//input[@id="Excel"]').click()
    acc_select = Select(driver.find_element(By.XPATH, '//select[@id="accountInfo"]'))
    acc_select.select_by_value('VALL')
    range_select = Select(driver.find_element(By.XPATH, '//select[@id="transactionDropDown"]'))
    range_select.select_by_value('N')
    time.sleep(2)
    driver.find_element(By.XPATH, '//a[@id="id_btn_continue"]').click()


try:
    try:
        login(driver)
        # waits for 2 step verification on phone
        # time.sleep(6)
    except:
        print("Unable to login")
    try:
        downloadcsv(driver)
    except:
        print("Something went wrong when downloading csv")
    driver.quit()
except:
    print("Invalid URL")