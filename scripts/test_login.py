import unittest

from parameterized import parameterized

from page.home_page import HomeBusiness
from utils import BaseDriver, DataDriven, BAS_URL


class Test_Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.homepage = HomeBusiness()
        BaseDriver.open_driver().get('https://www.imooc.com/')

    @classmethod
    def tearDownClass(cls):
        BaseDriver.close_driver()

    @parameterized.expand(DataDriven().create_dict(folder='/data/login.json'))
    def test_mukewang_login(self,username,pwd,msg):

        text_msg = self.homepage.home_mukewang_login(username,pwd)
        if text_msg == msg:
            print('登陆成功')
        else:
            print('登录失败')

if __name__ == '__main__':

    unittest.main()