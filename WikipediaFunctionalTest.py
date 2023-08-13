from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Chrome driver -> Chrome browser
service_obj = Service("D:\BrowserDrivers\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)


driver.get("https://www.wikipedia.org/")


# Basic article search
driver.maximize_window()
print(driver.title)
print(driver.current_url)


# //tag-name[@attribute='value'] -> //input[@type='search']
driver.find_element(By.XPATH, "//input[@type='search']").send_keys('Python programming')
driver.find_element(By.XPATH, "//button[@type='submit']").click()




def get_and_assert_article_title(driver1, assertion_text):
   article_title = driver.find_element(By.CLASS_NAME, 'mw-page-title-main').text
   print(article_title)
   assert assertion_text in article_title
   return article_title




# verify results in title and first paragraph
title1 = get_and_assert_article_title(driver, "Python (programming language)")
p1 = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(3) > div:nth-child(1) > div:nth-child(5) > "
                                         "main:nth-child(1) > div:nth-child(4) > div:nth-child(3) > "
                                         "div:nth-child(1) > p:nth-child(7)").text
print(p1)
assert ("Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code "
       "readability with the use of significant indentation.") in p1


# selecting an article and verifying title and first paragraph
driver.find_element(By.LINK_TEXT, "code readability").click()
title2 = get_and_assert_article_title(driver, "Computer programming")
p2 = driver.find_element(By.XPATH, "//p[contains(text(),'is the process of performing particular')]").text
print(p2)
assert "process of performing particular computations" in p2


# Go to main page and navigate to Talk Menu
driver.find_element(By.XPATH, "//a[@class='mw-logo']").click()  # clicking on logo should direct you to main menu
driver.find_element(By.XPATH, "//a[@title='Discuss improvements to the content page [alt-shift-t]']").click()
random_article = driver.find_element(By.XPATH, "//b[contains(text(),'This page is for discussing the contents of the "
                                              "En')]").text
print(random_article)
assert "Welcome! This page is for discussing the contents of the English Wikipedia's Main Page." in random_article


# interact with "random article" and verify
driver.find_element(By.XPATH, "//a[normalize-space()='Question help']").click()
title3 = get_and_assert_article_title(driver, "Questions")
p3 = driver.find_element(By.XPATH, "//p[2]").text
assert "Welcome to Wikipedia! This page lists some locations where you can ask questions or make comments." in p3


driver.close()