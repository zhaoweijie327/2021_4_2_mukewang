import parameterized

from base.base_actions import ActionsChains
from base.base_driver import BasePage, BaseHandles
from base.base_findeleme import FindElement

'''
对象层
'''
class HomePage(BasePage):

    def __init__(self):
        super().__init__()

    def home_find_element(self,loc,tag=3):
        try:
            element = self.find_element(loc,tag)
            return element
        except Exception as e:
            print("找不到元素：",e)

'''
操作层
'''
class HomeHandles(BaseHandles):

    def __init__(self):
        self.homepage = HomePage()
        self.action = ActionsChains()

    def home_login(self):
        '''
        点击首页登录
        :return:
        '''
        self.find_click(self.homepage.find_element(FindElement.home_login))

    def home_username(self,text):
        '''
        输入用户名
        :param text:
        :return:
        '''
        self.find_send_keys(self.homepage.find_element(FindElement.home_username),text)

    def home_pwd(self,text):
        '''
        输入密码
        :param text:
        :return:
        '''
        self.find_send_keys(self.homepage.find_element(FindElement.home_pwd),text)

    def home_button(self):
        '''
        点击登录
        :return:
        '''
        self.find_click(self.homepage.find_element(FindElement.home_button))

    def home_move_to(self):
        '''
        鼠标悬停到头像
        :return:
        '''
        self.action.action_move_to_element(self.homepage.find_element(FindElement.home_touxiang))

    def home_text(self):
        '''
        获取用户名
        :return:
        '''
        return self.find_text(self.homepage.find_element(FindElement.home_user))

class HomeBusiness:

    def __init__(self):
        self.homehandles = HomeHandles()


    def home_mukewang_login(self,username,pwd):
        self.homehandles.home_login()
        self.homehandles.home_username(username)
        self.homehandles.home_pwd(pwd)
        self.homehandles.home_button()
        self.homehandles.home_move_to()
        return self.homehandles.home_text()