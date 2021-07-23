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
        worse_elements = driver.find_elements_by_xpath("//table[@class='data-table']/tbody/tr/td[@data-type='worse']/span")
        actual = worse_elements[0].value_of_css_property("background-color")
        expected = Color.from_string('rgb(255, 225, 225)')
        self.assertEqual(actual, expected.rgb, 'Worse is not red')

    # Test data type better is green
    def test_better_shuould_be_green(self):
        better_elements = driver.find_elements_by_xpath("//table[@class='data-table']/tbody/tr/td[@data-type='better']/span")
        actual = better_elements[0].value_of_css_property("background-color")
        expected = Color.from_string('rgb(156, 244, 220)')
        self.assertEqual(actual, expected.rgb, 'Better is not green')

    # Test values above 0 are data type better
    def test_better_elements_are_better(self):
        better_elements = driver.find_elements_by_xpath("//table[@class='data-table']/tbody/tr/td[@data-type='better']/span")
        all_positive = True
        for i in (better_elements):
            value = i.get_attribute('textContent').replace('%','')
            if float(value) < 0:
               all_positive = False
        self.assertTrue(all_positive)

    # Test values below 0 are data type worse
    def test_worse_elements_are_worse(self):
        worse_elements = driver.find_elements_by_xpath("//table[@class='data-table']/tbody/tr/td[@data-type='worse']/span")
        all_negative = True
        for i in (worse_elements):
            value = i.get_attribute('textContent').replace('%','')
            if float(value) > 0:
                all_negative = False
        self.assertTrue(all_negative)

    # Test that all item in Change and Net Change are better or worse
    def test_change_columns_are_better_or_worse(self):
        worse_elements = driver.find_elements_by_xpath("//table[@class='data-table']/tbody/tr/td[@data-type='worse']/span")
        better_elements = driver.find_elements_by_xpath("//table[@class='data-table']/tbody/tr/td[@data-type='better']/span")
        net_change_col = driver.find_elements_by_xpath("//table[@class='data-table']/tbody/tr/td[2]/span")
        change_col = driver.find_elements_by_xpath("//table[@class='data-table']/tbody/tr/td[3]/span")
        expected = len(worse_elements) + len(better_elements)
        actual = len(net_change_col) + len(change_col)
        self.assertEqual(actual, expected, 'the number of better and worse is not equal to the total in the columns')

    @classmethod
    def tearDownClass(self):
        driver.close()
    
if __name__ == '__main__':
    unittest.main()