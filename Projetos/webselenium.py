from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = r"C:\driver\chromedriver.exe"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://quotes.toscrape.com/js")

# Encontra o primeiro autor (CORRETO no Selenium 4)
element = driver.find_element(By.XPATH, '//span[text()="woman"]')
print(element.text)

# Encontra todos os autores
elements = driver.find_elements(By.CLASS_NAME, "author")
for element in elements:
    print(element.text)

'''
element = driver.find_element_by_tag_name("small")
element = driver.find_element_by_id("abc")
element = driver.find_element_by_link_text("abc")
element = driver.find_element_by_xpath("//abc")
element = driver.find_element_by_css_selector(".abc")
'''
driver.quit()