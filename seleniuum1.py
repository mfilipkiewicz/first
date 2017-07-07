from selenium.webdriver import Edge
#from selenium.webdriver import Firefox


driver = Edge()
driver.get('www.wykop.pl/')

element = driver.find_element_by_partial_link_text('radziecki')

# element = driver.find_element_by_id("login")

element.click()
