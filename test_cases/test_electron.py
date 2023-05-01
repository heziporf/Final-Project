import allure
import pytest

from extensions.verifications import Verifications
from worksflows.electron_flows import ElectronFlows


@pytest.mark.usefixtures('init_electron_driver')
class TestElectron:
    @allure.title('Test 01: Add And Verify New Task')
    @allure.description('This test add a new task and verifies it in the list of tasks')
    def test_add_and_verify_new_task(self):
        ElectronFlows.add_new_task_flow('Learn JS')
        Verifications.verify_equals(ElectronFlows.get_number_of_tasks_flow(), 1)


    @allure.title('Test 02: Add And Verify New Tasks')
    @allure.description('This test adds a new tasks and verifies them in the list of tasks')
    def test_add_and_verify_new_tasks(self):
        ElectronFlows.add_new_task_flow('Learn Python')
        ElectronFlows.add_new_task_flow('Learn Java')
        ElectronFlows.add_new_task_flow('Learn C#')
        Verifications.verify_equals(ElectronFlows.get_number_of_tasks_flow(), 3)

    @allure.title('Test 03: Add And Verify New Tasks From a List')
    @allure.description('This test adds a new tasks and verifies them from a pre defined LIST')
    def test_add_and_verify_new_tasks_from_a_list(self):
        ElectronFlows.add_new_task_from_a_list_flow()
        Verifications.verify_equals(ElectronFlows.get_number_of_tasks_flow(), 10)

    def teardown_method(self):
        ElectronFlows.empty_list_flow()


