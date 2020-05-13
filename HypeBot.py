from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

def scroll_shim(passed_in_driver, object):
        x = object.location['x']
        y = object.location['y']
        scroll_by_coord = 'window.scrollTo(%s,%s);' % (
            x,
            y
        )
        scroll_nav_out_of_way = 'window.scrollBy(0, -240);'
        passed_in_driver.execute_script(scroll_by_coord)
        passed_in_driver.execute_script(scroll_nav_out_of_way)

# def check_cart(passed_in_driver):
#     # cart_count = passed_in_driver.find_element_by_xpath("//span[@class='cart-count-jewel small fs10-sm lh10-sm d-sm-b text-color-white bg-accent ta-sm-c']").getAttribute("innerHTML")
#     return cart_count

def clkButton(passed_in_driver, object):
    if 'firefox' in passed_in_driver.capabilities['browserName']:
        scroll_shim(passed_in_driver, object)
    
    passed_in_driver.implicitly_wait(500)

    add = ActionChains(passed_in_driver)
    add.move_to_element(object)
    add.click()
    add.perform()


driver = webdriver.Firefox()


passW = 'Bob9100t'
emailA = 'middletoncourt@gmail.com'


driver.get('https://www.nike.com/launch/t/kd13-hype')

# find the login button
login_box = driver.find_element_by_xpath("//button[@class='join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b']")

login_box.click()

# fetching the text boxes and submit button
email_box = driver.find_element_by_xpath("//div[@class = 'nike-unite-text-input emailAddress nike-unite-component empty']/input[1]")
password_box = driver.find_element_by_xpath("//div[@class = 'nike-unite-text-input password nike-unite-password-input nike-unite-component empty']/input[1]")
login_button = driver.find_element_by_xpath("//div[@class = 'nike-unite-submit-button loginSubmit nike-unite-component']/input[1]")

# # sending the info to the text boxes and clicking submit
email_box.send_keys(emailA)
password_box.send_keys(passW)
login_button.click()

# pick your size and add to cart
# while (check_cart(driver) < 1):
try:
    xpath = ("//button[starts-with(text(), 'M 11') or starts-with(text(), '11') and not(@disabled)]")
    size_btn = WebDriverWait(driver, 10).until(
            lambda driver : driver.find_element_by_xpath(xpath))
finally:
    print('size selected')

clkButton(driver, size_btn)

addToCart_btn = driver.find_element_by_xpath("//div[@class = 'mt2-sm mb6-sm prl0-lg fs14-sm']/button[1]")

clkButton(driver, addToCart_btn)


driver.get('https://www.nike.com/us/en/cart')

checkout_btn = driver.find_element_by_xpath("//button[contains(text(), 'Checkout')]")

clkButton(driver, checkout_btn)

placeOrder_btn = driver.find_element_by_xpath("//button[contains(text(), 'Place order')]")



