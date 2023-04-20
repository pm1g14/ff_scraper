from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from model import RowParameters
from utils import NumUtils as util
from utils import JsonUtils, DateUtils
import json
from datetime import date
from publisher import ZmqPublisher

def scrape(date:str):
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options = chrome_options)
    
    driver.get(f"http://www.forexfactory.com/calendar.php?day={date}")
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

if __name__ == '__main__':
    publisher =  ZmqPublisher()
    dateUtils = DateUtils()
    desiredDate = 'oct13.2022'
    nowDate = dateUtils.getNowDateInCorrectFormat()

    rows = scrape(date=desiredDate)
    filteredRows = filterRows(rows, "CPI", "USD")
    #send with zeromq
    message:dict = JsonUtils().convertListToJson(elements= filteredRows)
    publisher.publish(message=message)


#startlink = "calendar.php?day=nov18.2016"
#    baseURL = "http://www.forexfactory.com/"
#    r = requests.get(baseURL + startlink)
#    data = r.text
#    soup = BeautifulSoup(data, "lxml")
#    table = soup.find("table", class_="calendar__table")
#    trs = table.select("tr.calendar__row.calendar_row")
#    fields = ["date","time","currency","impact","event","actual","forecast","previous"]
#    curr_year = startlink[-4:]
#    curr_date = ""
#    curr_time = ""
#    for tr in trs:
#        try:
#            for field in fields:
#                data = tr.select("td.calendar__cell.calendar__{}.{}".format(field,field))[0]
#                # print(data)
#                if field=="date" and data.text.strip()!="":
#                    curr_date = data.text.strip()
#                elif field=="time" and data.text.strip()!="":
#                    # time is sometimes "All Day" or "Day X" (eg. WEF Annual Meetings)
#                    if data.text.strip().find("Day")!=-1:
#                        curr_time = "12:00am"
#                    else:
#                        curr_time = data.text.strip()
#                elif field=="currency":
#                    currency = data.text.strip()
#                elif field=="impact":
#                    # when impact says "Non-Economic" on mouseover, the relevant
#                    # class name is "Holiday", thus we do not use the classname
#                    impact = data.find("span")["title"]
#                elif field=="event":
#                    event = data.text.strip()
#                elif field=="actual":
#                    actual = data.text.strip()
#                elif field=="forecast":
#                    forecast = data.text.strip()
#                elif field=="previous":
#                    previous = data.text.strip()
#        except Exception as e:
#            print(e)