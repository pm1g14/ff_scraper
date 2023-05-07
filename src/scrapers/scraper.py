from selenium.webdriver.common.by import By
from model import RowParameters
from utils import NumUtils as util
from utils import JsonUtils, DateUtils
from datetime import date
import sys, time, datetime


class Scraper:

    def scrape(eventDate, driver):
        pass


class ForexFactoryScraper(Scraper):

    def scrape(self, eventDate, driver):
        driver.get(f"https://www.forexfactory.com/calendar.php?day={eventDate}")
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
    