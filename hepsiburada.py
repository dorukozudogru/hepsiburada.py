import time
from selenium import webdriver

driver = webdriver.Chrome("chromedriver.exe")
driver.maximize_window()
driver.get("https://hepsiburada.com")

driver.find_element_by_class_name("sf-OldMyAccount-PhY-T").click()
time.sleep(2)
driver.find_element_by_class_name("sf-OldMyAccount-32BWo").click()
time.sleep(4)
driver.find_element_by_xpath("//*[@id='txtUserName']").send_keys("pckobat-92@windowslive.com")
driver.find_element_by_xpath("//*[@id='txtPassword']").send_keys("Test123.")
time.sleep(2)
driver.find_element_by_xpath("//*[@id='btnLogin']").click()
time.sleep(4)
assert driver.find_element_by_class_name("hb-font-h1").text == "Hesabım"
time.sleep(2)
assert driver.find_element_by_css_selector("img[src$='yardimIcnKargo.jpg']")
driver.find_element_by_class_name("hb-logo").click()
assert driver.find_element_by_css_selector("img[src$='bannerImage2101_20210304131351.png']")

driver.get("https://www.hepsiburada.com/tasinabilir-diskler-c-100225")

assert driver.find_element_by_class_name("title").text == "Taşınabilir Disk Fiyatları"
assert driver.find_element_by_css_selector("img[src$='9845408596018.jpg']")

p1 = driver.find_element_by_xpath("//*[@id='i1']/div/a/h3").text
p2 = driver.find_element_by_xpath("//*[@id='i2']/div/a/h3").text

driver.find_element_by_xpath("//*[@id='i1']/div/a/div[2]/div[2]").click()
driver.find_element_by_xpath("//*[@id='i2']/div/a/div[2]/div[2]").click()
time.sleep(2)
driver.find_element_by_id("shoppingCart").click()
time.sleep(2)
items = driver.find_element_by_css_selector("#onboarding_item_list > ul").find_elements_by_tag_name("li")

#ul_list = driver.find_element_by_css_selector("#onboarding_item_list > ul")
#items = ul_list.find_elements_by_tag_name("li")
count = 0
for item in items:
    if str.__contains__(item.text, p1):
        count += 1
    if str.__contains__(item.text, p2):
        count += 1
assert count == 2
