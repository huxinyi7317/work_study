from selenium.webdriver.support.ui import WebDriverWait

def yuansu_dw(driver,list,timeout=60):

    return WebDriverWait(driver=driver,timeout=timeout).until(lambda s: s.find_element(*list))