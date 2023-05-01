import allure

from extensions.db_actions import DBActions
from worksflows.web_flows import WebFlows


class DBFlows:
    @staticmethod
    @allure.step('Login to Grafana via database flow')   # change
    def login_grafana_via_db():
        columns = ['name', 'password']
        result = DBActions.get_query_result(columns, 'Employees', 'comments', 'correct')
        WebFlows.login_flows(result[0][0], result[0][1])