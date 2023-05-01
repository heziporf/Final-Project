import allure
import pytest


from utilities.common_ops import get_data
from worksflows import web_flows
from worksflows.web_flows import WebFlows


@pytest.mark.usefixtures('init_web_driver')
class Test_Web:
    @allure.title('Test01: Verify Search Item')
    @allure.description('this test search an item and verify it after')
    def test_search_for_item(self):
        WebFlows.search_for_item(get_data('Item'))
        WebFlows.verify_search_title("Search Results for: " + get_data('Item'))

    @allure.title('Test02: Verify Menu Buttons')
    @allure.description('this test verify the menu buttons are displayed')
    def test_verify_upper_menu(self):
        WebFlows.verify_menu_buttons_flow_smart_assertions()     # smart-assertions


    @allure.title('Test03: Verify Adding To Cart')
    @allure.description('this test loops through products and print if is in / out of stock')
    def test_adding_to_cart(self):
        WebFlows.looping_through_items()

    @allure.title('Test04: Verify Number Of Items After Searching')
    @allure.description('this test verify that the numbers of items are corresponding to the search results')
    @pytest.mark.parametrize('search_value',  web_flows.testdata)
    def test_csv(self, search_value):
        WebFlows.search_items_in_store(search_value)


    @pytest.mark.parametrize('search_value, expected_items', web_flows.testdata)
    def test_csv(self, search_value, expected_items):
        WebFlows.search_items_in_store(search_value)
        WebFlows.verify_search_result(int(expected_items))


