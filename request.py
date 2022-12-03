from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

login = "https://world.taobao.com/wow/z/oversea/SEO-SEM/ovs-pc-login"

# driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chrome')
# driver.get('https://translate.google.com.hk/?hl=zh-TW&tab=TT')

options =  webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)

def googleSearch():
    driver.maximize_window()
    driver.get("http://www.google.com")

    # Find the html element
    element = driver.find_element(by=By.CLASS_NAME, value='gLFyf')
    # Input the string and press enter 
    element.send_keys('Selenium Python', Keys.RETURN)
    
googleSearch()