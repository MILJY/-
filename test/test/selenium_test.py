from selenium.webdriver import Chrome, Keys
from selenium.webdriver.common.by import By
from chaojiying import Chaojiying_Client
import time

web=Chrome()

web.get("http://www.lagou.com")

web.find_element(By.CLASS_NAME,value='tab').click()#切换城市
time.sleep(1)

web.find_element(By.ID,value='search_input').send_keys("c++",Keys.ENTER)#搜索c++岗位
time.sleep(1)

web.find_element(By.CLASS_NAME,value='p-top__1F7CL').click()
time.sleep(1)

web.switch_to.window(web.window_handles[-1])
job_detail=web.find_element(By.CLASS_NAME,value='job_bt').text
print(job_detail)
time.sleep(1)

web.close()
web.switch_to.window(web.window_handles[0])

job_list=web.find_elements(By.CLASS_NAME,value="item__10RTO")
for it in job_list:
    job_company=it.find_element(By.CLASS_NAME,value="company-name__2-SjF").text
    job=it.find_element(By.CLASS_NAME,value='p-top__1F7CL').find_element(By.TAG_NAME,value='a').text
    job_price=it.find_element(By.CLASS_NAME,value='money__3Lkgq').text
    print(job_company,job,job_price)