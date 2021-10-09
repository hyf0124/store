import time
from selenium import  webdriver

from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get(r'F:/自动化框架/练习的html/滑动验证/mousedrag.html')

driver.maximize_window()


a = driver.find_element_by_class_name('slider')

ActionChains(driver).drag_and_drop_by_offset(a,248,0).perform()


time.sleep(3)

driver.quit()