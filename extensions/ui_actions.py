
import allure
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
import test_cases.conftest as conf  # create shortcut for static method (mouse_hover)



class UiActions:
    @staticmethod
    @allure.step('click on element')
    def click(elem: WebElement):
        elem.click()

# yoni call it UPDATE TEXT
    @staticmethod
    @allure.step('updating text')
    def send_keys(elem: WebElement, value: str):
        elem.send_keys(value)

    @staticmethod
    @allure.step('mouse hover tooltip')  # one element mouse hover
    def mouse_hoser_tooltip(elem: WebElement):
        ActionChains(conf.driver).move_to_element(elem).click().perform() # because that electron always refresh
        # itself, we need to reset all the time here for it to work



    @staticmethod
    @allure.step('mouse hover two elements')
    def mouse_hover(elem1: WebElement, elem2: WebElement):
        conf.action.move_to_element(elem1).move_to_element(elem2).click().perform()

    @staticmethod
    @allure.step('Press Keyboard key')
    def press_key(key:Keys):
        conf.action.send_keys(key).perform()

    @staticmethod
    @allure.step('right click on element')
    def right_click(elem: WebElement):
        conf.action.context_click(elem).perform()


    @staticmethod
    @allure.step('drag and drop')
    def drag_and_drop(elem1: WebElement, elem2: WebElement):
        conf.action.drag_and_drop(elem1, elem2).perform()

    @staticmethod
    @allure.step('clear text field in element')
    def clear(elem: WebElement):
        elem.clear()


    @staticmethod
    @allure.step('go back to last page')
    def back():
        conf.driver.back()

    @staticmethod
    @allure.step('go back twice(in page)')
    def double_back():
        conf.driver.back()
        conf.driver.back()
