from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())


passW = ''
emailA = ''


driver.get('https://www.nike.com/launch/t/kd13-hype')

# find the login button
login_box = driver.find_element_by_xpath("//button[@class='join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b']")
driver.implicitly_wait(10)
login_box.click()

# fetching the text boxes and submit button
email_box = driver.find_element_by_xpath("//div[@class = 'nike-unite-text-input emailAddress nike-unite-component empty']/input[1]")
password_box = driver.find_element_by_xpath("//div[@class = 'nike-unite-text-input password nike-unite-password-input nike-unite-component empty']/input[1]")
login_button = driver.find_element_by_xpath("//div[@class = 'nike-unite-submit-button loginSubmit nike-unite-component']/input[1]")

# # sending the info to the text boxes and clicking submit
email_box.send_keys(emailA)
password_box.send_keys(passW)
login_button.click()

# pick your size
size_btn = driver.find_element_by_xpath("//button[contains(text(), 'M 11') or contains(text(), '11')]")

driver.implicitly_wait(10)
ActionChains(driver).move_to_element(size_btn).click(size_btn).perform()



