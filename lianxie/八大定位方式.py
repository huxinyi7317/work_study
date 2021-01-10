from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path=r'driver\chromedriver.exe')

driver.get('http://dev.echronos.com:10514')
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/form/div[1]/div/div[1]/input').send_keys('15179745797')
sleep(2)
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys('111111')
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/form/button').click()

sleep(3)

driver.find_element_by_xpath('//div[text()="商品上架"]').click()
sleep(3)

driver.quit()
