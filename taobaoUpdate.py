from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time


# driver = webdriver.Chrome()

options =  webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

def login():
    # 打开淘宝登录页，并进行扫码登录
    driver.get("https://ithelp.ithome.com.tw/articles/10277352")
    time.sleep(3)
    temp = driver.find_element(by=By.LINK_TEXT, value="技術問答")
    print(temp)
    if temp:
        temp.click()

    



if __name__ == "__main__":
    # times = input("请输入抢购时间：")
    # 时间格式："2018-09-06 11:20:00.000000"
    login()
    # buy("2021-08-24 14:30:00.000000")
