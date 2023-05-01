import allure
from selenium.webdriver.remote.webelement import WebElement
from smart_assertions import soft_assert, verify_expectations


class Verifications:
    @staticmethod
    @allure.step('verify ACTUAL result is equal to EXPECTED result ')
    def verify_equals(actual, expected):
        assert actual == expected, 'Verify Equals Failed, Actual: ' + str(actual) + ' is not Equals to Expected: ' + str(expected)
#
    @staticmethod
    @allure.step('verify that element is displayed ')
    def is_displayed(elem: WebElement):
        assert elem.is_displayed(), 'Verify is Displayed Failed, Element: ' + elem.text + 'is not Displayed'
#
    # Verify Menu Button Using smart-assertions
    @staticmethod
    @allure.step('soft verifications(assert) of elements using soft assertions ')
    def soft_assert(elems):
        for i in range(len(elems)):
            soft_assert(elems[i].is_displayed())
        verify_expectations()
#
#
    @staticmethod
    @allure.step('verify number of elements in list ')
    def verify_number_of_elements(elems, size):
        assert len(elems) == size, 'number of elements in the list: ' +str(len(elems)) + 'does not match expected' +str(size)
#
