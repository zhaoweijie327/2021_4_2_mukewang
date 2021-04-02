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
    # 定位密码
    home_pwd = (By.CSS_SELECTOR,"[placeholder='请输入密码']")
    # 定位登录
    home_button = (By.CSS_SELECTOR,'.moco-btn')
    # 定位头像
    home_touxiang = (By.CSS_SELECTOR,'#header-avator')
    # 用户名
    home_user = (By.CSS_SELECTOR,'.card-top-right-box .text-ellipsis')