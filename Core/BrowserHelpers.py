from Core.BaseClass import BaseClass
from Core.Locators import Locator
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BrowserHelpers(BaseClass, Locator):

    def find_element(self, object_locator):
        self.parse_locator(object_locator)
        if self.locator:
            find = {
                "id": getattr(self.driver, 'find_element_by_id'),
                "xpath": getattr(self.driver, 'find_element_by_xpath'),
                "css": getattr(self.driver, 'find_element_by_css_selector'),
            }
            method = find[self.locator_type]
            element = method(self.locator)
        return element

    def find_elements(self, object_locator):
        elements = None
        self.parse_locator(object_locator)
        if self.locator:
            find = {
                "id": getattr(self.driver, 'find_elements_by_id'),
                "xpath": getattr(self.driver, 'find_elements_by_xpath'),
                "css": getattr(self.driver, 'find_elements_by_css_selector'),
            }
            method = find[self.locator_type]
            elements = method(self.locator)
        return elements

    def enter_text(self, object_locator, text, delay_typing=False, delay_in_seconds=0.5):
        self.find_element(object_locator).clear()
        if not delay_typing:
            self.find_element(object_locator).send_keys(text)
        else:
            for char in text:
                self.find_element(object_locator).send_keys(char)
                time.sleep(delay_in_seconds)

    def enter_key(self, object_locator, keys):
        self.find_element(object_locator).send_keys(keys)
        time.sleep(1)

    def click_on(self, object_locator, *, using_javascript=False):
        return self.find_element(object_locator).click()

    def get_text(self, object_locator):
        text = self.find_element(object_locator).text
        self.info_log(f"{self.locator_description} has text: '{text}'")
        return text

    def is_element_present(self, object_locator):
        status = False
        try:
            self.wait_time(2)
            element = self.find_element(object_locator)
            status = element.is_displayed()
        except Exception:
            status = False
        return status

    def wait_for_element(self, object_locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(object_locator)
        )

    def navigate_to_url(self, url):
        self.driver.get(url)
        self.wait_time(5)
        self.info_log(f"Navigate To '{url}'")

    def wait_time(self, time_in_seconds):
        time.sleep(time_in_seconds)

    def mouse_hover(self, object_locator):
        element = self.find_element(object_locator)
        ActionChains(self.driver).move_to_element(
            element).perform()
