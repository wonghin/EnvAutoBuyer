from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
 
 
class Login:
    def __init__(self, username, password):
        self.url = 'https://login.taobao.com/member/login.jhtml'
        # initialize browser
        options = webdriver.ChromeOptions()
        # prohibite downloading image 
        options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
        # set developing mode
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # set options
        self.browser = webdriver.Chrome(options=options)
        # wait browser 40s
        self.wait = WebDriverWait(self.browser, 40)
        self.username = username  # 用户名
        self.password = password  # 密码
 
    def original(self):
 
        self.browser.get(url=self.url)
        try:
            input_username = self.wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, 'div.fm-field > div.input-plain-wrap.input-wrap-loginid > input'
            )))
            input_password = self.wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, 'div.fm-field > div.input-plain-wrap.input-wrap-password > input'
            )))
            # 等待滑块按钮加载
            div = self.wait.until(EC.presence_of_element_located((
                By.ID, 'nc_1__bg'
            )))
            print("input_username_element: ")
            print(input_username)
            
            print("input_password_element: ")
            print(input_password)
            input_username.send_keys(self.username)
            input_password.send_keys(self.password)
            # wait 10s 
            time.sleep(10)
            # # 点击并按住滑块
            # ActionChains(self.browser).click_and_hold(div).perform()
            # # 移动滑块
            # ActionChains(self.browser).move_by_offset(xoffset=300, yoffset=0).perform()
            # # 等待验证通过
            # self.wait.until(EC.text_to_be_present_in_element((
            #     By.CSS_SELECTOR, 'div#nc_1__scale_text > span.nc-lang-cnt > b'), '验证通过'
            # ))
            # # 登录
            # input_password.send_keys(Keys.ENTER)
            # print('Successful !')
        except TimeoutException as e:
            print('Error:', e.args)
            self.original()
 
    def sina(self):
        """
        使用新浪微博账号登录（提前绑定新浪账号）
 
        :return: None
        """
        self.browser.get(url=self.url)
        try:
            # 等待新浪登录链接加载
            weibo_login = self.wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, '#login-form a.weibo-login'
            )))
            weibo_login.click()
            input_username = self.wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, 'div.info_list > div.inp.username > input.W_input'
            )))
            input_password = self.wait.until(EC.presence_of_element_located((
                By.CSS_SELECTOR, 'div.info_list > div.inp.password > input.W_input'
            )))
            input_username.send_keys(self.username)
            input_password.send_keys(self.password)
            input_password.send_keys(Keys.ENTER)
            # 等待浏览器保存我方信息，网速不好可以设置长一点
            time.sleep(5)
            # 刷新页面
            self.browser.refresh()
            # 等待快速登录按钮加载
            quick_login = self.wait.until(EC.element_to_be_clickable((
                By.CSS_SELECTOR, 'div.info_list > div.btn_tip > a.W_btn_g'
            )))
            quick_login.click()
            print('login successful !')
        except TimeoutException as e:
            print('Error:', e.args)
            self.sina()
            
