from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome('chromedriver.exe')
driver.get("https://1st.smart-factory.kr/login.do")


driver.find_element_by_xpath("/html/body/div[1]/div/div/div[1]/span[2]/a").click()
id = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/form/dl/dd[1]/input')
id.send_keys("tipa103")
pw=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/form/dl/dd[2]/input')
pw.send_keys("rlwjddnjs@123")

driver.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/div[1]/a').click()

driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div[1]/div[1]/a[1]").click()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[1]/ul/li[3]/a').click()
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[1]/div[1]/ul/li[3]/div/a[1]').click()

#driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[6]/div[1]/div[3]/div[1]/a').click()


driver.execute_script('javascript:void(0)')

"""
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
"""