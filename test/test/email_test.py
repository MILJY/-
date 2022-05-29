from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

#打开登录界面
option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
web = webdriver.Chrome(options=option)
web.get('https://mail.163.com/')
time.sleep(2)

div=web.find_element(By.CLASS_NAME,value='loginUrs')
#得到登录框的iframe
iframe=div.find_element(By.TAG_NAME,value='iframe')
web.switch_to.frame(iframe)

#账号
web.find_element(By.NAME,value='email').send_keys("MHB20010614@163.com")
#密码
web.find_element(By.NAME,value='password').send_keys("NISHIZHUMA520")
#登录
web.find_element(By.ID,value='dologin').click()
web.switch_to.default_content()
time.sleep(2)


#点击写信
web.find_element(By.ID,value='_mail_component_149_149').click()
time.sleep(2)

#收件人
web.find_element(By.CLASS_NAME,value='nui-editableAddr-ipt').send_keys("1497446614@qq.com",Keys.ENTER)
time.sleep(1)
#主题
web.find_elements(By.CLASS_NAME,value='nui-ipt-input')[-2].send_keys("测试")

#得到内容框的iframe
editor_iframe=web.find_element(By.CLASS_NAME,value='APP-editor-iframe')
web.switch_to.frame(editor_iframe)
web.find_element(By.CLASS_NAME,value='nui-scroll').send_keys("你好，你妈叫你回家吃饭")
web.switch_to.default_content()
time.sleep(2)

web.find_element(By.ID,value='_mail_icon_37_282').click()
time.sleep(3)

web.find_element(By.ID,value='_mail_tabitem_0_133text').click()
time.sleep(1)

