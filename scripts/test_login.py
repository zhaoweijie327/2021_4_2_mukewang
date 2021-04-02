import unittest

from page.home_page import HomeBusiness
from utils import BaseDriver


class Test_Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.homepage = HomeBusiness()
        BaseDriver.open_driver().get('https://www.imooc.com/')

    @classmethod
    def tearDownClass(cls):
        BaseDriver.close_driver()

    def test_mukewang_login(self):
        username = '15015754120'
        pwd = 'kg83200477'
        msg = '招伟杰'
        text_msg = self.homepage.home_mukewang_login(username,pwd)
        if text_msg == msg:
            print('登陆成功')
        else:
            print('登录失败')

if __name__ == '__main__':

    unittest.main()