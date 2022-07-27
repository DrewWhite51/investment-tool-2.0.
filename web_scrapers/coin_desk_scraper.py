from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup


class CoinDeskScraper:
    # Need to clean this method up, writing these scrapers will be harder than what I thought
    def home_page_scraper(self):

        CHROMEDRIVER_PATH = "C:/Users/drew_/OneDrive/Desktop/chromedriver_win32/chromedriver.exe"
        scrape_url = f'https://www.coindesk.com/'
        options = Options()
        options.headless = True
        options.add_argument("--window-size=1920,1200")

        driver = webdriver.Chrome(options=options, executable_path=CHROMEDRIVER_PATH)
        driver.get(scrape_url)

        soup = BeautifulSoup(driver.page_source, 'lxml')

        sections = soup.findAll('section')

        for data in soup.findAll('a', href=True):
            print(data)
        print(len(sections))

        for section in sections:
            print(section.findAll('a'))
            for anchors in section.findAll('a'):
                print(anchors['href'])

        driver.quit()

    def business_scraper(self):
        pass

    def tech_scraper(self):
        pass

    def policy_scraper(self):
        pass

    def markets_scraper(self):
        pass