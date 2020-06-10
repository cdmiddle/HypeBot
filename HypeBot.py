import time
from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from random import randrange

class NormalPurchase:

    driver = webdriver.Firefox()
    passW = ''
    emailA = ''
    shoe_size = ''
    cvv = ''
    release_date = ''
    product_url = ''

    def __init__(self, password, email, shoesize, cvv, releasedate, producturl):
        super().__init__()
        NormalPurchase.passW = password
        NormalPurchase.emailA = email
        NormalPurchase.shoe_size = shoesize
        NormalPurchase.cvv = cvv
        # NormalPurchase.release_date = datetime.strptime('releasedate' + ' 10:00 AM', '%b %d %Y %I:%M%p')
        NormalPurchase.release_date = datetime.strptime(releasedate + ' 9:44PM', '%b %d %Y %I:%M%p')
        NormalPurchase.product_url = producturl
        self.login()
        self.select_size()
        self.checkout()

    @staticmethod
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

    @staticmethod
    def clk_button(passed_in_driver, object):
        if 'firefox' in passed_in_driver.capabilities['browserName']:
            NormalPurchase.scroll_shim(passed_in_driver, object)

        add = ActionChains(passed_in_driver)
        add.move_to_element(object)
        add.click()
        add.perform()

    @staticmethod
    def wait_for_invisibility(object):
        try:
            while(object.is_displayed()):
                pass
        except StaleElementReferenceException as e:
            pass
        time.sleep(1)

    @staticmethod
    def capture_page(driver, name):
        with open(name, "x") as f:
            f.write(driver.page_source)

    @staticmethod
    def find_element(xpath):
        try:
            button = WebDriverWait(NormalPurchase.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            return button
        except TimeoutError:
            print('timedout :/ : ' + xpath)


    def login(self):
        self.driver.get(self.product_url)
        # find the login button
        login_icon = NormalPurchase.find_element("//button[@class='join-log-in text-color-grey prl3-sm pt2-sm pb2-sm fs12-sm d-sm-b']")
        login_icon.click()
        # fetching the text boxes and submit button
        email_box = NormalPurchase.find_element("//div[@class = 'nike-unite-text-input emailAddress nike-unite-component empty']/input[1]")
        password_box = NormalPurchase.find_element("//div[@class = 'nike-unite-text-input password nike-unite-password-input nike-unite-component empty']/input[1]")
        login_button = NormalPurchase.find_element("//div[@class = 'nike-unite-submit-button loginSubmit nike-unite-component']/input[1]")
        # sending the info to the text boxes and clicking submit
        email_box.send_keys(self.emailA)
        password_box.send_keys(self.passW)
        NormalPurchase.clk_button(self.driver, login_button)
        login_window = NormalPurchase.find_element("//div[@class = 'ncss-col-sm-12 full bg-white ta-sm-r']")
        NormalPurchase.wait_for_invisibility(login_window)
        # wait until the release time and then refresh the page
        now = datetime.now()
        sleep_time = abs(self.release_date - now) if abs(self.release_date - now).seconds < 0 else 0
        time.sleep(sleep_time)
        

    def select_size(self):
        self.driver.refresh()
        # # pick your size and add to cart
        size_btn = NormalPurchase.find_element("//button[starts-with(text(), 'M " + self.shoe_size + "') or starts-with(text(), " + self.shoe_size + ")]")
        # capture_page(driver, 'clcik.html')
        NormalPurchase.clk_button(self.driver, size_btn)
        addToCart_btn = NormalPurchase.find_element("//div[@class = 'mt2-sm mb6-sm prl0-lg fs14-sm']/button[1]")
        # NormalPurchase.capture_page(self.driver, 'addtocart.html')
        NormalPurchase.clk_button(self.driver, addToCart_btn)
        proceed = NormalPurchase.find_element("//div[@class = 'cart-item-modal-content-container ncss-container p6-sm bg-white']")

    def checkout(self):
        self.driver.get('https://www.nike.com/us/en/cart')
        checkout_btn = NormalPurchase.find_element("//div[@class = 'ncss-col-sm-12 css-gajhq5']/button[@class = 'css-8k8rmj e1qel1sl4']")
        # capture_page(driver, "checkout.html")
        NormalPurchase.clk_button(self.driver, checkout_btn)
        # interact with the iframe for credit card info
        try :
            # a special case, sometimes the cvv code is required, possibly when the card has been used by another acount in recent history
            iframe = NormalPurchase.find_element_by_xpath("//iframe[@class = 'redit-card-iframe-cvv mt1 u-full-width']")
            self.driver.switch_to.frame(iframe)
            cvv_input = NormalPurchase.find_element("//input[@class = 'mod-input ncss-input pt2-sm pr4-sm pb2-sm pl4-sm']")
            cvv_input.send_keys(self.cvv)
            self.driver.switch_to.default_content()
        except AttributeError:
            pass
        placeOrder_btn = NormalPurchase.find_element("//button[@class = 'd-lg-ib fs14-sm ncss-brand ncss-btn-accent pb2-lg pb3-sm prl5-sm pt2-lg pt3-sm u-uppercase']")
        # capture_page(driver, "order.html")
        NormalPurchase.clk_button(self.driver, placeOrder_btn)



