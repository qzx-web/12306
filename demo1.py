# -*- coding: utf-8 -*-
from selenium import  webdriver

#测试一下
class Qiangpiao(object):
    driver_path = r"C:\Users\qzx\Desktop\pachong\demo\ajax\chromedriver.exe"
    def __init__(self):
        self.login_url = "https://kyfw.12306.cn/otn/resources/login.html"
        self.initma_url = ""
        self.driver = webdriver.Chrome(executable_path=self.driver_path)

    def _login(self):
        self.driver.get(self.login_url)

    def _order_ticket(self):
        pass

    def run(self):
        self._login()
        self._order_ticket()

if __name__ == '__main__':
    spider = Qiangpiao()
    spider.run()