import unittest
from selenium import webdriver
from selenium.webdriver.support.color import Color
driver = webdriver.Firefox(executable_path=r'C:\Users\Daniel G\Downloads\geckodriver.exe')

#  Old setup test
#  driver.get("https://www.bloomberg.com/markets/currencies")
#  EUR_USD_Change_Value = driver.find_element_by_xpath("//table[@class='data-table']/tbody/tr[1]/td[2]/span").text
#  EUR_USD_Change_Color = 
#  driver.close()
#  print (EUR_USD_Change)


class CurrencyConverter(unittest.TestCase):
    def setUp(self):
        driver.get("https://www.bloomberg.com/markets/currencies")
        #  print("open webpage success")

    # Test data type worse is red
    def test_worse_should_be_red(self):
        #  print('worseShouldBeRed executed')
        
        worseElements = driver.find_elements_by_xpath("//table[@class='data-table']/tbody/tr/td[@data-type='worse']/span")
        actual = worseElements[0].value_of_css_property("background-color")
        expected = Color.from_string('rgb(255, 225, 225)')
        self.assertEqual(actual, expected.rgb, 'Worse is not red')

        #  print(len(worseElements))
        #  print(worseElements[0].value_of_css_property("background-color"))

    # Test data type better is green
    # Test values above 0 are data type better
    # Test values below 0 are data typer worse
    
    def tearDown(self):
        driver.close()
        #  print("close webpage success")
    
if __name__ == '__main__':
    unittest.main()