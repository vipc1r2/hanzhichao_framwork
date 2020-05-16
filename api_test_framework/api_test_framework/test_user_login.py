import unittest  # 导入unittest
import requests


class TestUserLogin(unittest.TestCase):  # 类必须Test开头，继承TestCase才能识别为用例类
    url = 'http://115.28.108.130:5000/api/user/login/'

    def test_user_login_normal(self):  # 一条测试用例，必须test_开头
        data = {"name": "张三", "password": "123456"}
        res = requests.post(url=self.url, data=data)
        self.assertIn('登录成功', res.text)  # 断言

    def test_user_login_password_wrong(self):
        data = {"name": "张三", "password": "1234567"}
        res = requests.post(url=self.url, data=data)
        self.assertIn('用户名或密码错误', res.text)  # 断言


if __name__ == '__main__':
    unittest.main(verbosity=2)
