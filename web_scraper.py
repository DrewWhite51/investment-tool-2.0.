from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

PATH = "C:/Users/drew_/OneDrive/Desktop/chromedriver_win32/chromedriver.exe"

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=PATH)
driver.get("https://finance.yahoo.com/quote/NVDA?p=NVDA&.tsrc=fin-srch")
# print(driver.page_source)

soup = BeautifulSoup(driver.page_source,'lxml')

print(soup.find_all('div'))

driver.quit()
