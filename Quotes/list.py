from selenium import webdriver

driver = webdriver.Chrome("C:\\Users\\user\\Documents\\chromedriver.exe")
driver.get("https://motivationping.com/quotes/")
elements = driver.find_elements_by_css_selector('div.container p strong')
length = len(elements)
for i in range(length):
    print (elements[i].text())


