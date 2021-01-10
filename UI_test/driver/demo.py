from selenium import webdriver
from time import sleep
from UI_test.tools.utils import Tools

#添加订单
driver = webdriver.Chrome(executable_path='driver\chromedriver.exe')
driver.get('http://dev.echronos.com:10460/personal/work_platform/')
driver.implicitly_wait(10)
#driver.maximize_window()
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/form/div[1]/div/div[1]/input').send_keys('15179745797')
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys('111111')
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/form/button/span').click()
# driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div/div[4]').click()
# #for a in range(100):
# # driver.switch_to_frame()
# shuru = driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[1]/div[2]/div[1]/div/div[4]/div/span/div[2]/div[1]/div[1]/div/div')
# shuru.send_keys('cs')

sleep(5)
t = Tools()
t.A()

driver.quit()
