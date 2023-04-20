from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import requests

def scrape():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options = chrome_options)
    
    driver.get("http://www.forexfactory.com/calendar.php?day=nov18.2016")
    table = driver.find_element(By.CLASS_NAME, "calendar__table")
    for row in table.find_elements(By.TAG_NAME, "tr"):
    
        event = row.find_element(By.XPATH, "//td[@class='calendar__cell calendar__event event']").text
        actual = row.find_element(By.XPATH, "//td[@class='calendar__cell calendar__actual actual']").text
        forecast = row.find_element(By.XPATH, "//td[@class='calendar__cell calendar__forecast forecast']").text
        previous = row.find_element(By.XPATH, "//td[@class='calendar__cell calendar__previous previous']").text
        currency = row.find_element(By.XPATH, "//td[@class='calendar__cell calendar__currency currency ']").text
        time = row.find_element(By.XPATH, "//td[@class='calendar__cell calendar__time time']").text
        date = row.find_element(By.XPATH, "//td[@class='calendar__cell calendar__date date']").text
        print(td.tag_name)
        print(td.text)
        
        #if row_data == []:
        #    continue
        #print(row_data)
    


if __name__ == '__main__':
    scrape()



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