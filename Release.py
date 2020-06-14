import time
from datetime import datetime
from HypeBot import NormalPurchase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Release(NormalPurchase):

    passW = ''
    emailA = ''
    shoe_size = ''
    cvv = ''
    release_date = ''
    product_url = ''

    def __init__(self, password, email, shoesize, cvv, releasedate, producturl, interwebdriver):
        self.release_date = releasedate
        super().__init__(password, email, shoesize, cvv, producturl, interwebdriver)

    def select_size(self):
        # wait until the release time and then refresh the page
        release_date = datetime.strptime(self.release_date + " 10:00AM", '%b %d %Y %I:%M%p')
        now = datetime.now()
        sleep_time = abs(release_date - now) if abs(release_date - now).seconds < 0 else 0
        time.sleep(sleep_time)
        self.driver.refresh()
        # # pick your size and add to cart
        size_btn = NormalPurchase.find_element(self.driver, "//button[starts-with(text(), 'M " + self.shoe_size + "') or starts-with(text(), " + self.shoe_size + ")]")
        NormalPurchase.capture_page(self.driver, 'release_size')
        NormalPurchase.clk_button(self.driver, size_btn)
        addToCart_btn = NormalPurchase.find_element(self.driver, "//div[@class = 'mt2-sm mb6-sm prl0-lg fs14-sm']/button[1]")
        NormalPurchase.capture_page(self.driver, 'release_addtocart')
        NormalPurchase.clk_button(self.driver, addToCart_btn)
        # if checkout modal is not loaded, the checkout button probably didn't get clicked
        try:
            checkout_modal = WebDriverWait(self.driver, 2).until(EC.element_to_be_present((By.XPATH, "//div[@class = 'checkout-modal']")))
        except (NoSuchElementException, AttributeError):
            super().checkout()


    def checkout(self):
        # selects the first radio button corresponding to an address
        shipping_addr = Release.find_element(self.driver, "//div[@class='checkout-shipping-section-content prl6-sm prl0-md checkout-section-expandable ']/div[@class='ncss-radio-container']/input[1]")
        Release.clk_button(self.driver, shipping_addr)
        shipping_options = Release.find_element(self.driver, "//div[@class='checkout-shipping-section-content prl6-sm prl0-md checkout-section-expandable ']/input[@id = 'STANDARD']")
        Release.clk_button(self.driver, shipping_options)
        save_and_continue = Release.find_element(self.driver, "//button[text()='Save & Continue']")
        Release.clk_button(self.driver, shipping_options)
        # selects the first credit card on file
        cc_radio = Release.find_element(self.driver, "//div[@class='payment-component mt1-sm']/div[@class='ncss-radio-container']/input[1]")
        Release.clk_button(self.driver, cc_radio)
        submit_order = Release.find_element(self.driver, "//div[@class='payment-component mt1-sm']/button[text()='Submit Order']")
        Release.clk_button(self.driver, submit_order)



