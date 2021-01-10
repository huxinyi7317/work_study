from selenium import webdriver
from time import sleep

#添加订单
driver = webdriver.Chrome(executable_path='driver\chromedriver.exe')
driver.get('https://www.huacaigou.com/accounts/login?next=/')
driver.implicitly_wait(10)
#driver.maximize_window()
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/form/div[1]/div/div[1]/input').send_keys('15179745797')
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/form/div[2]/div/div[1]/input').send_keys('111111')
driver.find_element_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/form/button/span').click()
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[4]/i').click()
driver.find_element_by_xpath('//*[@id="wrap"]/div[1]/div/div[1]/div/div/div/div[1]/div[2]/span').click()
driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[1]/div[1]/div/div[1]/div[2]/div/div/div[1]/label/span[1]/span').click()
driver.find_element_by_xpath('//*[@id="wrap"]/div[2]/div[2]/div[2]/button/span').click()
sleep(3)
driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[2]/div[1]/div/div[2]/div[2]/div[2]/button').click()
driver.find_element_by_xpath('//*[@id="app"]/div[3]/div[2]/div[1]/div/div[8]/div/div[2]/div/div[1]/div/div[1]/div').click()
driver.find_element_by_xpath('//*[@id="addr_form"]/div[1]/div/div/div/span/span/i').click()
#点击地址北京
sleep(2)
lb = driver.find_element_by_xpath("//li[@class='el-cascader-node']").click()

lb = driver.find_element_by_xpath('//div[@class="el-popper el-cascader__dropdown"]/div/div[2]/div/ul/li').click()


lb = driver.find_element_by_xpath('//div[@class="el-popper el-cascader__dropdown"]/div/div[3]/div/ul/li[1]').click()

driver.find_element_by_xpath('//*[@id="addr_form"]/div[2]/div/div[1]/input').send_keys('测试测试123')
driver.find_element_by_xpath('//*[@id="addr_form"]/div[3]/div/div[1]/input').send_keys('测试')
driver.find_element_by_xpath('//*[@id="addr_form"]/div[4]/div/div[1]/input').send_keys('15120000000')
driver.find_element_by_xpath('//*[@id="addr_form"]/div[6]/div/label/span[1]/span').click()
driver.find_element_by_xpath('//*[@id="addr_form"]/div[7]/button').click()



sleep(3)
driver.quit()