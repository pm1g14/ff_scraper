import random
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from model import RowParameters
from utils import NumUtils as util
from utils import JsonUtils, DateUtils
import sys, time
from datetime import date
from publisher import ZmqPublisher

def scrape(date:str, driver):
    
    driver.get(f"https://www.forexfactory.com/calendar.php?day={date}")
    table = driver.find_element(By.CLASS_NAME, "calendar__table")
    rows = []
    index = 2
    
    for row in table.find_elements(By.TAG_NAME, "tr"):    
            try:
                index += 1
        
                event = row.find_element(By.XPATH, f"//*[@id='flexBox_flex_calendar_mainCal']/table/tbody/tr[{index}]/td[6]").text
                actual = row.find_element(By.XPATH, f"//*[@id='flexBox_flex_calendar_mainCal']/table/tbody/tr[{index}]/td[8]").text
                forecast = row.find_element(By.XPATH, f"//*[@id='flexBox_flex_calendar_mainCal']/table/tbody/tr[{index}]/td[9]").text
                previous = row.find_element(By.XPATH, f"//*[@id='flexBox_flex_calendar_mainCal']/table/tbody/tr[{index}]/td[10]").text
                currency = row.find_element(By.XPATH, f"//*[@id='flexBox_flex_calendar_mainCal']/table/tbody/tr[{index}]/td[4]").text
                time = row.find_element(By.XPATH, f"//*[@id='flexBox_flex_calendar_mainCal']/table/tbody/tr[{index}]/td[2]").text
                date = row.find_element(By.XPATH, f"//*[@id='flexBox_flex_calendar_mainCal']/table/tbody/tr[{index}]/td[1]").text.replace('\n', ' ')
                if date == '':
                    date = rows[0].date

                if ("%" in actual):
                    actual = actual.replace('%', '')
                if "%" in forecast:
                    forecast = forecast.replace('%', '')
                if "%" in previous:
                    previous = previous.replace('%', '')

                if ("B" in actual):
                    actual = actual.replace('B', '')
                if "B" in forecast:
                    forecast = forecast.replace('B', '')
                if "B" in previous:
                    previous = previous.replace('B', '')
                rowParams = RowParameters(
                    date = date, 
                    time = time, 
                    currency = currency, 
                    event = event, 
                    actual = util.stringToFloat(actual), 
                    forecast = util.stringToFloat(forecast),
                    previous = util.stringToFloat(previous)
                )
                rows.append(rowParams)
            
            except Exception as e:
                print(e)
                continue
    driver.close()        
    return rows

    
def filterRows(rows: RowParameters, event:str, curr:str):
    filtered = []
    for row in rows:
        if (event in row.event):
            filtered.append(row)
    return filtered


def getDriver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options = chrome_options)
    return driver


if __name__ == '__main__':
    publisher =  ZmqPublisher()

    dateUtils = DateUtils()
    # desiredDate = 'oct13.2022'
    nowDate = date.today()
    nowDateFormatted = dateUtils.getDateInCorrectFormat(date=nowDate)

    if (nowDateFormatted != ''):
        while True:
            driver = getDriver()
            rows = scrape(date=nowDateFormatted, driver= driver)
            filteredRows = filterRows(rows, "CPI", "USD")
            #send with zeromq
            message:dict = JsonUtils().convertListToJson(elements= filteredRows)
            if rows:
                publisher.publish(message=message)

            time.sleep(10)

    else:
        sys.exit()
