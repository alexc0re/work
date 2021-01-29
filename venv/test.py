import unittest
from selenium import webdriver
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
class MyTestCase(unittest.TestCase):
    def test_something(self):
        links = "topbitcoinsera"
        driver.get("http://"+ links + ".dev8.leaddist.team")


if __name__ == '__main__':
    unittest.main()
