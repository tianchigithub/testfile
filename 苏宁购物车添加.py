from selenium import webdriver
import time

# 打开浏览器
driver = webdriver.Chrome()

# 页面最大化
driver.maximize_window()

# 进入苏宁页面
driver.get("http://www.suning.com")

# 搜索联想
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("联想")
driver.find_element_by_xpath('//*[@id="searchSubmit"]').click()

# 选中联想
driver.find_element_by_xpath('//*[@id="0010336548-12113598936"]/div/div/div[1]/div/a/i/img').click()

# 跳转到第二页面
datas = driver.window_handles
driver.switch_to.window(datas[1])

# 添加到购物车
driver.find_element_by_xpath('//*[@id="addCart"]').click()
driver.find_element_by_xpath('/html/body/div[38]/div/div[2]/div/div[1]/a').click()

# 退出浏览器
time.sleep(3)
driver.quit()