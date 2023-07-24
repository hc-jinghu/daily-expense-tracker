import os
import gspread
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# figure out .env
chromedriver = "/chromedriver"
option = webdriver.ChromeOptions()
option.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'

s = Service(chromedriver)
driver = webdriver.Chrome(service=s, options=option)


load_dotenv()
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

driver.get("https://secure.royalbank.com/statics/login-service-ui/index#/full/signin?LANGUAGE=ENGLISH")
breakpoint()
