import time
import allure
from selenium.webdriver.common.keys import Keys
import page_objects.web_objects.search_results as s_results
import utilities.manage_pages as page
from extensions.ui_actions import UiActions
from extensions.verifications import Verifications
from page_objects.web_objects import store
from utilities.common_ops import wait, For, get_data, read_csv

data = read_csv(get_data('CSV_Location'))
testdata = [
    (data[0][0], data[0][1]),
    (data[1][0], data[1][1]),
    (data[2][0], data[2][1])
]
class WebFlows:
    @staticmethod
    @allure.step('login to grafana flows')   # for db testing
    def login_flows(user:str, password : str):
        UiActions.send_keys(page.web_login_page_grafana.get_user_name(), user)
        UiActions.send_keys(page.web_login_page_grafana.get_password(), user)
        UiActions.click(page.web_login_page_grafana.get_submit())
        UiActions.click(page.web_login_page_grafana.get_skip())

    @staticmethod
    @allure.step('verify grafana title flows')   # for db testing
    def verify_grafana_title(expected: str):
        actual = page.main_page_grafana.get_main_title().text
        Verifications.verify_equals(actual, expected)


    @staticmethod
    @allure.step('search an item from the main page of the site flow')
    def search_for_item(search_item: str):
        UiActions.click(page.web_header.get_search())
        UiActions.send_keys(page.web_header.get_search_input(), search_item)
        time.sleep(2)
        UiActions.click(page.web_header.get_search_after_click())

    @staticmethod
    @allure.step('verify search title flow')
    def verify_search_title(expected: str):
        wait(For.ELEMENT_EXISTS, s_results.search_results)
        actual = page.web_search.get_search_results().text
        Verifications.verify_equals(actual, expected)

    # Verify Menu Button Using smart-assertions
    @staticmethod
    @allure.step('verify displayed menu buttons using smart assertions')
    def verify_menu_buttons_flow_smart_assertions():
        elems = [page.web_header.get_home_button(),
                 page.web_header.get_store_button(),
                 page.web_header.get_men_button(),
                 page.web_header.get_women_button(),
                 page.web_header.get_accessories(),
                 page.web_header.get_about(),
                 page.web_header.get_contact()
                 ]
        Verifications.soft_assert(elems)

    # my solution
    @staticmethod
    @allure.step('looping through items list and checking if product is in stock flow')
    def looping_through_items():
        UiActions.click(page.web_header.get_store_button())  # click to start in STORE in the site
        for i in range(len(page.web_store.get_list_of_items())):
            item_text = page.web_store.get_list_of_items()[i].text
            UiActions.click(page.web_store.get_list_of_items()[i])
            if (len(page.web_store.get_add_to()) > 0):
                print(item_text + " is in stock")
            else:
                print(item_text + "is out of stock")
            UiActions.click(page.web_header.get_store_button())  # click to start in STORE in the site

    @staticmethod
    @allure.step('search items in store and verify number of search results flow')
    def search_items_in_store(search_value):
        UiActions.click(page.web_header.get_store_button())
        UiActions.clear(page.web_store.get_search_button())
        UiActions.send_keys(page.web_store.get_search_button(), search_value)
        UiActions.press_key(Keys.ENTER)

    @staticmethod
    def verify_search_result(expected):
        wait(For.ELEMENT_EXISTS, store.search_button)
        actual = len(page.web_search.search_results_in_store_search())
        Verifications.verify_equals(actual, expected)

