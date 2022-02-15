from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

mail = 'sjyet96@kiria.org'
name = '테스트'

options= webdriver.ChromeOptions()
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")


driver = webdriver.Chrome('C:/Users/TETRA/Desktop/autocheck/chromedriver.exe',options=options)
driver.get("https://mail.kiria.org/index.ds")


id = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/form/fieldset/div[1]/div[1]/input')
id.send_keys("sjyet96")
pw=driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/form/fieldset/div[1]/div[2]/input')
pw.send_keys("Songjiyou!1")

driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/form/fieldset/div[2]/input').click()
time.sleep(3)

#driver.find_element_by_xpath('/html/body/form[1]/div[3]/div/div[1]/div[1]/div/ul/li[1]/a/span').click()
driver.execute_script('javascript: mailWrite();')
#time.sleep(2)


#driver.find_element_by_css_selector('#mainDiv > div > table.mail_write > tbody > tr:nth-child(1) > td.rec > textarea').send_keys("sjyet96@kiria.org,")
#driver.find_element_by_css_selector('#mainDiv > div > table.mail_write > tbody > tr:nth-child(4) > td > textarea').send_keys("제목없음")


#element = driver.find_element_by_id("freeRTE")
#driver.switch_to.frame(element)
#driver.find_element_by_css_selector('body').send_keys("내용입력\n내용 두번째 줄 \n\n두줄띄우기")
#driver.switch_to.default_content() #처음 상태로 되돌아옴
#driver.find_element_by_xpath('/html/body/form[1]/div[1]/div/div[3]/div/div[2]/div/a[1]').click()

"""
driver.find_element_by_xpath('/html/body/form[1]/div[3]/div/div[1]/div[1]/div/ul/li[1]').click()


driver.find_element_by_xpath('/html/body/form[1]/div[1]/div/div[3]/div/table[1]/tbody/tr[1]/td[1]/textarea').send_keys(mail)
driver.find_element_by_xpath('/html/body/form/div/table/tbody/tr[1]/td/input[1]').click()

"""