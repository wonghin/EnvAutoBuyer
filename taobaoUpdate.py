from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import time
from selenium.webdriver.common.keys import Keys
import accountDetails as user
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# driver = webdriver.Chrome()

options =  webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()

def login():
    # 打开淘宝登录页，并进行扫码登录
    driver.get("https://www.taobao.com")
    onLoginPage = driver.find_element(by=By.LINK_TEXT, value="亲，请登录")
    time.sleep(3)
    # print(onLoginPage)
    if onLoginPage:
        onLoginPage.click()
        

    
    
    inputLoginId = driver.find_element(by=By.CSS_SELECTOR('div.fm-field > div.input-plain-wrap.input-wrap-loginid > input'))
    print(inputLoginId)
    inputLoginId.send_keys(user.loginId)
    
 
    # inputPassword = driver.find_element(by=By.CSS_SELECTOR, value='div.fm-field > div.input-plain-wrap.input-wrap-password > input')
    # print(inputPassword)
    # inputPassword.send_keys(user.password)
    
   



if __name__ == "__main__":
    # times = input("请输入抢购时间：")
    # 时间格式："2018-09-06 11:20:00.000000"
    login()
    # buy("2021-08-24 14:30:00.000000")
