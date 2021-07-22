from selenium import webdriver
driver = webdriver.Firefox(executable_path=r'C:\Users\Daniel G\Downloads\geckodriver.exe')

#  Old setup test
#  driver.get("https://www.bloomberg.com/markets/currencies")
#  EUR_USD_Change_Value = driver.find_element_by_xpath("//table[@class='data-table']/tbody/tr[1]/td[2]/span").text
#  EUR_USD_Change_Color = 
#  driver.close()
#  print (EUR_USD_Change)


class currencyConverter:
    # setup
    # Test data type worse is red
    # Test data type better is green
    # Test values above 0 are data type better
    # Test values below 0 are data typer worse
    # clean up

    def setup():
        driver.get("https://www.bloomberg.com/markets/currencies")
        print("open webpage success")
    
    def cleanUp():
        driver.close()
        print("close webpage success")
    
    

cc = currencyConverter
cc.setup()
cc.cleanUp()
    
    # driver.get("https://www.bloomberg.com/markets/currencies")
    # if (datatype worse is equal to red):
    #    return True