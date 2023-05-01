import time
import allure
from selenium.webdriver.common.keys import Keys
import utilities.manage_pages as page
from extensions.ui_actions import UiActions


class ElectronFlows:
    @staticmethod
    @allure.step('Add New Task Flow')
    def add_new_task_flow(task_name):
        UiActions.send_keys(page.electron_task.get_create(), task_name)
        UiActions.send_keys(page.electron_task.get_create(), Keys.RETURN)


    @staticmethod
    @allure.step('Get Number Of Tasks')
    def get_number_of_tasks_flow():
        return len(page.electron_task.get_tasks())


    @staticmethod
    @allure.step('Empty Task From List Flow')
    def empty_list_flow():
        for x in range(ElectronFlows.get_number_of_tasks_flow()):
            time.sleep(0.5)
            UiActions.mouse_hoser_tooltip(page.electron_task.get_delete_buttons()[0])


    @staticmethod
    @allure.step('Add New Task Flow From a list')
    def add_new_task_from_a_list_flow():
        task_name_from_a_list = ['Java', 'Python', 'Rubi', 'JS', 'C#', 'C++', 'Perl', 'Rust', 'Swift ', 'Kotlin']
        for i in range(len(task_name_from_a_list)):
            UiActions.send_keys(page.electron_task.get_create(), "Learn " + task_name_from_a_list[i])
            UiActions.send_keys(page.electron_task.get_create(), Keys.RETURN)
        return len(task_name_from_a_list)

