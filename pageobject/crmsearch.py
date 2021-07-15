import os
from page.Base import base
from selenium.webdriver.common.by import By
f = os.path.abspath('../data/data.txt')
with open(f, 'r', encoding='utf-8') as file:
    lines = file.readlines()
    a = []
    for line in lines:
        c = line.split('\n')
        b = c[0].split(',')
        a.append(b)
class crmsearch(base):
    def c_login1(self):
        return self.find(By.name, "userNum",a)
    def c_login2(self):
        return self.find(By.name,"userPw")
