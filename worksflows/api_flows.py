import allure

from extensions.api_actions import APIActions
from utilities.common_ops import get_data

url = get_data('Url_Api')


class ApiFlows:
    @staticmethod
    @allure.step('Create new user in "reqres.in" flow')
    def create_user(id, email, first_name, last_name, avatar):
        payload = {
                    "id": id,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "avatar": avatar
        }
        status_code = APIActions.post(url + 'api/users', payload)
        return status_code

    @staticmethod
    @allure.step('Update user in "reqres.in" flow')
    def update_user(email, first_name, last_name, avatar, id):
        payload = {
                    "id": id,
                    "email": email,
                    "first_name": first_name,
                    "last_name": last_name,
                    "avatar": avatar
        }
        status_code = APIActions.put(url + 'api/users/2' + str(id), payload)
        return status_code


    @staticmethod
    @allure.step('Delete user in "reqres.in" flow')
    def delete_user(id):
        status_code = APIActions.delete(url + 'api/users/2' + str(id))
        return status_code