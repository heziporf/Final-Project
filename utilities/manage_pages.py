import test_cases.conftest as conf
from page_objects.desktop_objects.standard_page import StandardPage
from page_objects.electron_objects.task_page import TaskPage
from page_objects.mobile_objects.calculator_page import CalculatorPage
from page_objects.mobile_objects.saved_page import SavedPage
from page_objects.web_objects.header import Header
from page_objects.web_objects.home_page import HomePage
from page_objects.web_objects.main_page_grafana import MainPageGrafana
from page_objects.web_objects.search_results import Search
from page_objects.web_objects.store import Store
from page_objects.web_objects.login_page_grafana import LoginPage

#Web_objects

web_home = None
web_header = None
web_store = None
web_search = None

#Web_objects / grafana
web_login_page_grafana = None
main_page_grafana = None

#Mobile_objects
mobile_calculator = None
mobile_saved = None

#Electron_objects
electron_task = None

#Desktop_objects
standard_clac = None

class ManagePages:
    @staticmethod
    def init_web_pages():
        globals()['web_home'] = HomePage(conf.driver)
        globals()['web_header'] = Header(conf.driver)
        globals()['web_store'] = Store(conf.driver)
        globals()['web_search'] = Search(conf.driver)
        globals()['web_login_page_grafana'] = LoginPage(conf.driver)
        globals()['main_page_grafana'] = MainPageGrafana(conf.driver)

    @staticmethod
    def init_mobile_pages():
        globals()['mobile_calculator'] = CalculatorPage(conf.driver)
        globals()['mobile_saved'] = SavedPage(conf.driver)

    @staticmethod
    def init_electron_pages():
        globals()['electron_task'] = TaskPage(conf.driver)

    @staticmethod
    def init_desktop_pages():
        globals()['standard_clac'] = StandardPage(conf.driver)