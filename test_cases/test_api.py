import allure

from extensions.verifications import Verifications
from worksflows.api_flows import ApiFlows
id = 7
email = 'hezi@gmail.com'
first_name = 'hezi'
last_name = 'zalait'
avatar = 'https://reqres.in/img/faces/4-image.jpg'


class TestApi:
    @allure.title('Test 01 : Create User And Verify Status Code')
    @allure.description('this test create user a new user in "reqres.in"')
    def test_create_and_verify_user(self):
        actual = ApiFlows.create_user(id, email, first_name, last_name, avatar)
        Verifications.verify_equals(actual, 201)



    @allure.title('Test 02 : Update User And Verify Status Code ')
    @allure.description('this test update user and verify status code"')
    def test_update_and_verify_user_name(self):
        actual = ApiFlows.update_user(email, first_name + 'kuku', last_name, avatar, id)
        Verifications.verify_equals(actual, 200)

    @allure.title('Test 03 : Delete User And Verify Status Code ')
    @allure.description('this test delete User and verify status code"')
    def test_delete_user(self):
        actual = ApiFlows.delete_user(5)
        Verifications.verify_equals(actual, 204)