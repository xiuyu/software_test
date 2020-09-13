from appium import  webdriver


desired_caps = {}

desired_caps['platformName'] = 'Android'

desired_caps['platformVersion'] = '8.1.0'

desired_caps['deviceName'] = 'test'

desired_caps['appPackage'] = 'com.xiuyu.appiumtest'

desired_caps['appActivity'] = 'com.xiuyu.appiumtest.MainActivity'

desired_caps["unicodeKeyboard"] = True

desired_caps["resetKeyboard"] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 点击测试按钮
driver.find_element_by_id('com.xiuyu.appiumtest:id/btn_go').click()
# 输入
driver.find_element_by_id('com.xiuyu.appiumtest:id/et_input').send_keys('hello word')
