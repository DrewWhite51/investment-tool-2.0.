from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re

PATH = "C:/Users/drew_/OneDrive/Desktop/chromedriver_win32/chromedriver.exe"

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=PATH)
# print(driver.page_source)
NVDA = "https://finance.yahoo.com/quote/NVDA?p=NVDA&.tsrc=fin-srch"
SQ = "https://finance.yahoo.com/quote/SQ?p=SQ&.tsrc=fin-srch"

driver.get(SQ)

soup = BeautifulSoup(driver.page_source,'lxml')

current_price_data = soup.find("div", {"id": "mrt-node-Lead-5-QuoteHeader"})
current_str = str(current_price_data)

quote_data = soup.findAll("tr")

# print((soup.prettify()))

price_movement = (re.findall(r'"\d+\.\d+"', current_str))
price_mov = {
    'current_price': (price_movement[0]),
    'dollar_move': (price_movement[1]),
    'percent_move': (price_movement[2]),
    'after_hours_price': (price_movement[3]),
    'after_hours_dollar_move': (price_movement[4]),
    'after_hours_percent_move':(price_movement[5])
}

table_rows = []
for row in quote_data:
    table_rows.append(str(row.text.strip()))

quotes = {
    'previous_close': float(table_rows[0][14:]),
    'open': table_rows[1][4:],
    'bid': table_rows[2][3:],
    'ask': table_rows[3][3:],
    'day_range': table_rows[4][11:],
    'year_range': table_rows[5][13:],
    'volume': table_rows[6][6:],
    'average_volume': table_rows[7][11:],
    'market_cap': table_rows[8][10:],
    'beta_5y_monthly': table_rows[9][17:],
    'pe_ratio': table_rows[10][14:],
    'eps': table_rows[11][9:],
    'earnings_date': table_rows[12][13:],
    'forward_dividend_and_yield': table_rows[13][24:],
    'one_year_estimate': table_rows[15][13:]
}

stock_information = {
    'price_movement': price_mov,
    'quotes': quotes
}


driver.quit()
