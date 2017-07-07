from selenium.webdriver import Edge
import random
driver = Edge()



driver.get("https://www.igame.com/eye-test/")

driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
score = 0
if score > 0 and score < 9:
    co_wybrac = random.randint(0, 1)
    if co_wybrac == 0
    el = driver.find_element_by_class_name("thechosenone")
el.click()

