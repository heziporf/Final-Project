import allure
import pytest

from extensions.verifications import Verifications

from worksflows.desktop_flows import DesktopFlows




@pytest.mark.usefixtures('init_desktop_driver')
class TestDesktop:
    @allure.title('Test 01: Adding Two Numbers')
    @allure.description('This test adds two numbers and verify the results')
    def test_add_numbers_and_verify(self):
        DesktopFlows.calculate_flow('1+7')
        Verifications.verify_equals(DesktopFlows.get_result_flow(), '8')

    @allure.title('Test 02: Aritmatic Actions')
    @allure.description('This test does some aritmatic actions and verifies it')
    def test_aritmatic_actions(self):
        DesktopFlows.calculate_flow('2*5+50/2-25')
        Verifications.verify_equals(DesktopFlows.get_result_flow(), '5')

    @allure.title('Test 03: Aritmatic Actions From a Pre Defined Random Numbers And Operator Generator')
    @allure.description('This test does some aritmatic actions in a random way and verifies it')
    def test_aritmatic_actions_random(self):
        DesktopFlows.calculate_flow(DesktopFlows.calculate_flow_random_numbers_and_operators())
        DesktopFlows.get_print_flow()


    def teardown_method(self):
        DesktopFlows.clear_flow()
