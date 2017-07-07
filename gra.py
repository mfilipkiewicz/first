from selenium.webdriver import Edge
from modul import get_driver


driver = get_driver()

driver.get("https://www.igame.com/eye-test/")

driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

for i in range (30):
    el = driver.find_element_by_class_name("thechosenone")
    print(el)
    #el.click()

    #el = firefox.find_element_by_partial_link_text('radziecki')
#el.click()