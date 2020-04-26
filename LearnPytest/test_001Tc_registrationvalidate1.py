from selenium.webdriver import Firefox

driver = webdriver.Firefox(executable_path="//Users//nareshmanhas//Desktop//Selenium//geckodriver")
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('https://www.facebook.com/')