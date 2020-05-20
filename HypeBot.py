import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


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

def capture_page(driver, name):
    with open(name, "x") as f:
        f.write(driver.page_source)



driver = webdriver.Firefox()


passW = 'Bob9100t'
emailA = 'middletoncourt@gmail.com'
shoe_size = '13'


driver.get('https://www.nike.com/launch/t/acg-moc-3-0-tie-dye')

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


# # pick your size and add to cart
# # while (check_cart(driver) < 1)

time.sleep(1)

try:
    xpath = ("//button[starts-with(text(), 'M 11') or starts-with(text(), '11') and not(@disabled)]")
    # size_btn = WebDriverWait(driver, 10).until(
    #         lambda driver : driver.find_element_by_xpath(xpath))
    size_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[starts-with(text(), 'M " + shoe_size + "') or starts-with(text(), " + shoe_size + ") and not(@disabled)]")))
    capture_page(driver, "size.html")
finally:
    print('size selected')

clk_button(driver, size_btn)


addToCart_btn = driver.find_element_by_xpath("//div[@class = 'mt2-sm mb6-sm prl0-lg fs14-sm']/button[1]")

capture_page(driver, 'addtocart.html')

clk_button(driver, addToCart_btn)


driver.get('https://www.nike.com/us/en/cart')

try:
    xpath = ("//div[@class = 'ncss-col-sm-12 css-gajhq5']/button[@class = 'css-8k8rmj e1qel1sl4']")
    # size_btn = WebDriverWait(driver, 10).until(
    #         lambda driver : driver.find_element_by_xpath(xpath))
    checkout_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
    capture_page(driver, "cart.html")
except TimeoutError:
    print('took too long')

# checkout_btn = driver.find_element_by_xpath("//div[@class = 'ncss-col-sm-12 css-gajhq5']/button[@class = 'css-8k8rmj e1qel1sl4']")
# capture_page(driver, "checkout.html")

clk_button(driver, checkout_btn)

# email_entry = driver.find_element_by_xpath("//input[@name = 'emailAddress']")
# pass_entry = driver.find_element_by_xpath("//input[@name = 'password']")
# login_button = driver.find_element_by_xpath("//input[@value = 'MEMBER CHECKOUT']")

# email_entry.send_keys(emailA)
# pass_entry.send_keys(passW)
# clk_button(login_button)


# placeOrder_btn = driver.find_element_by_xpath("//button[contains(text(), 'Place order')]")



