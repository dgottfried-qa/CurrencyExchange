import unittest
from selenium import webdriver
from selenium.webdriver.support.color import Color
driver = webdriver.Firefox(executable_path=r'C:\Users\Daniel G\Downloads\geckodriver.exe')

class CurrencyConverter(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        driver.get("https://www.bloomberg.com/markets/currencies")

    # Test data type worse is red
    def test_worse_should_be_red(self):
        worseElements = driver.find_elements_by_xpath("//table[@class='data-table']/tbody/tr/td[@data-type='worse']/span")
        actual = worseElements[0].value_of_css_property("background-color")
        expected = Color.from_string('rgb(255, 225, 225)')
        self.assertEqual(actual, expected.rgb, 'Worse is not red')

    # Test data type better is green
    def test_better_shuould_be_green(self):
        better_elements = driver.find_elements_by_xpath("//table[@class='data-table']/tbody/tr/td[@data-type='better']/span")
        actual = better_elements[0].value_of_css_property("background-color")
        expected = Color.from_string('rgb(156, 244, 220)')
        self.assertEqual(actual, expected.rgb, 'Better is not green')

    # Test values above 0 are data type better
    # Test values below 0 are data typer worse
    
    @classmethod
    def tearDownClass(self):
        driver.close()
    
if __name__ == '__main__':
    unittest.main()