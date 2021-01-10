#cls的用法
import unittest

class A(unittest.TestCase):
    name = '胡新宜'
    @classmethod
    def setUpClass(cls):
        cls.name = '我是类启动'
        print(cls.name)

    @classmethod
    def tearDownClass(cls):
        print('test结束')

    def setUp(self):
        print('我是方法启动')
    def test_01(self):
        print(self.name)
if __name__ == "__main__":
    unittest.main()