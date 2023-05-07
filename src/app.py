from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from model import RowParameters
from utils import NumUtils as util
from utils import JsonUtils, DateUtils
import sys, time
from datetime import date
from publisher import ZmqPublisher
from scrapers.scraper import ForexFactoryScraper

    
def filterRows(rows: RowParameters, event:str, curr:str):
    filtered = []
    for row in rows:
        if (event in row.event):
            filtered.append(row)
    return filtered


def getDriver():
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options = chrome_options)
    return driver


if __name__ == '__main__':
    publisher =  ZmqPublisher()
    ff_scraper = ForexFactoryScraper()

    dateUtils = DateUtils()
    desiredDate = 'oct13.2022'
    nowDate = date.today()
    nowDateFormatted = dateUtils.getDateInCorrectFormat(date=nowDate)

    if (nowDateFormatted != ''):
        while True:
            driver = getDriver()
            rows = ff_scraper.scrape(nowDateFormatted, driver)
            #send with zeromq
            message:dict = JsonUtils().convertListToJson(elements= rows)
            if rows:
                publisher.publish(message=message)

            time.sleep(3)

    else:
        sys.exit()
