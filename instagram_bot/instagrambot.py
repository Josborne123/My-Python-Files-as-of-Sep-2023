from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By



# browser = webdriver.Chrome()
# Choosing what browser to use
browser = webdriver.Firefox()

# Sets five seconds of waiting time. If Selenium can’t find an element, then it waits for five seconds to allow everything to load and tries again.
browser.implicitly_wait(5)

# Getting the url
browser.get('https://www.instagram.com/')
sleep(2)


# These 2 lines below are not needed because the default page for instagram now is a login page
#login_link = browser.find_element_by_xpath("//a[text()='Log in']")
#login_link.click()


# Find the cookies button and click accept all to get rid of the cookies popup thing
cookies_button = browser.find_element(By.XPATH, '//button[text()="Accept All"]')
cookies_button.click()


# Find username and password inputs by CSS. There are other methods that you can use (https://selenium-python.readthedocs.io/locating-elements.html)
username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

# Inputting your username and password
username_input.send_keys("convolvulus3")
password_input.send_keys("waterballtapestarwars1234")

# Finding the login button and then clicking it.
login_button = browser.find_element_by_xpath("//button[@type='submit']")
browser.execute_script("arguments[0].click();", login_button)

# Choosing not to save info when the save info butotn pops up.
saveinfo_button = browser.find_element(By.XPATH, '//button[text()="Not Now"]')
saveinfo_button.click()

# Choosing the not now option when the turn on notifications section pops up
###notification_button = browser.find_element(By.XPATH, '//button[text()="Not Now"]')
###notification_button.click()




	

#sleep(10)

# Closing the browser
#browser.close()