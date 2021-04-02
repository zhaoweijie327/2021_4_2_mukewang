'''
存放定位元素

'''
from selenium.webdriver.common.by import By


class FindElement:

    # ..........................首页..........................
    # 定位登录元素
    home_login = (By.CSS_SELECTOR,'#js-signin-btn')
    # 定位用户名
    home_username = (By.CSS_SELECTOR,"[placeholder='请输入登录手机号/邮箱']")