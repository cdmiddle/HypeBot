import time
import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from random import randrange


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


def clk_button(passed_in_driver, object):
    if 'firefox' in passed_in_driver.capabilities['browserName']:
        scroll_shim(passed_in_driver, object)

    add = ActionChains(passed_in_driver)
    add.move_to_element(object)
    add.click()
    add.perform()

    # out = object.get_attribute('outerHTML')
    # inner = object.get_attribute('innerHTML')


# wait for object to disappear on webpage
def wait_for_invisibility(object):
    try:
        while(object.is_displayed()):
            pass
    except StaleElementReferenceException as e:
        pass
    time.sleep(1)

def capture_page(driver, name):
    with open(name, "x") as f:
        f.write(driver.page_source)


def find_element(xpath):
    try:
        button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
        return button
    except TimeoutError:
        print('timedout :/')



driver = webdriver.Firefox()


passW = 'Bob9100t'
emailA = 'middletoncourt@gmail.com'
shoe_size = '13'
cvv = '132'
release_date = datetime.datetime(2020, 5, 21, 17, 59)
now = datetime.datetime.now()


driver.get('https://www.nike.com/launch/t/pg-4-pcg')

# find the login button
login_icon = driver.find_element_by_xpath("//button[@class='join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b']")

login_icon.click()

# fetching the text boxes and submit button
email_box = driver.find_element_by_xpath("//div[@class = 'nike-unite-text-input emailAddress nike-unite-component empty']/input[1]")
password_box = driver.find_element_by_xpath("//div[@class = 'nike-unite-text-input password nike-unite-password-input nike-unite-component empty']/input[1]")
login_button = driver.find_element_by_xpath("//div[@class = 'nike-unite-submit-button loginSubmit nike-unite-component']/input[1]")

# sending the info to the text boxes and clicking submit
email_box.send_keys(emailA)
password_box.send_keys(passW)
login_button.click()

login_window = driver.find_element_by_xpath("//div[@class = 'ncss-col-sm-12 full bg-white ta-sm-r']")

wait_for_invisibility(login_window)

# wait until the release time and then refresh the page
# time.sleep((release_date - now).seconds)

driver.refresh()


# # pick your size and add to cart

size_btn = find_element("//button[starts-with(text(), 'M " + shoe_size + "') or starts-with(text(), " + shoe_size + ")]")
# capture_page(driver, 'clcik.html')


clk_button(driver, size_btn)


addToCart_btn = find_element("//div[@class = 'mt2-sm mb6-sm prl0-lg fs14-sm']/button[1]")

# capture_page(driver, 'addtocart.html')

clk_button(driver, addToCart_btn)


driver.get('https://www.nike.com/us/en/cart')

checkout_btn = find_element("//div[@class = 'ncss-col-sm-12 css-gajhq5']/button[@class = 'css-8k8rmj e1qel1sl4']")

# capture_page(driver, "checkout.html")

clk_button(driver, checkout_btn)


iframe = find_element("//iframe[@class = 'credit-card-iframe-cvv mt1 u-full-width']")

driver.switch_to.frame(iframe)

cvv_input = find_element("//input[@class = 'mod-input ncss-input pt2-sm pr4-sm pb2-sm pl4-sm']")

cvv_input.send_keys(cvv)

driver.switch_to.default_content()

# placeOrder_btn = driver.find_element_by_xpath("//button[contains(text(), 'Place order')]")
placeOrder_btn = find_element("//button[@class = 'd-lg-ib fs14-sm ncss-brand ncss-btn-accent pb2-lg pb3-sm prl5-sm pt2-lg pt3-sm u-uppercase']")
# capture_page(driver, "order.html")
clk_button(driver, placeOrder_btn)



