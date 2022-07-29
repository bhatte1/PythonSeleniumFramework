from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Users/vinayakbhatte/Java/chromedriver")
driver.get("https://rahulshettyacademy.com/AutomationPractice")


driver.maximize_window()

List1 = driver.find_elements_by_xpath("//input[@type = 'radio']")

for e in List1:
 if e.get_attribute("value") == 'radio2':
  e.click()
  assert e.is_selected()


driver.switch_to.frame()

