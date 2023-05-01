import allure
import random


from extensions.ui_actions import UiActions
import utilities.manage_pages as page

class DesktopFlows:
    @staticmethod
    @allure.step('Calculate Equation')
    def calculate_flow(equation):
        for i in equation:
            DesktopFlows.calculator_click(i)
        UiActions.click(page.standard_clac.get_equals())


    @staticmethod
    def calculator_click(value):
        if value == '0':
            UiActions.click(page.standard_clac.get_zero())
        elif value == '1':
            UiActions.click(page.standard_clac.get_one())
        elif value == '2':
            UiActions.click(page.standard_clac.get_two())
        elif value == '3':
            UiActions.click(page.standard_clac.get_three())
        elif value == '4':
            UiActions.click(page.standard_clac.get_four())
        elif value == '5':
            UiActions.click(page.standard_clac.get_five())
        elif value == '6':
            UiActions.click(page.standard_clac.get_six())
        elif value == '7':
            UiActions.click(page.standard_clac.get_seven())
        elif value == '8':
            UiActions.click(page.standard_clac.get_eight())
        elif value == '9':
            UiActions.click(page.standard_clac.get_nine())
        elif value == '+':
            UiActions.click(page.standard_clac.get_plus())
        elif value == '-':
            UiActions.click(page.standard_clac.get_minus())
        elif value == '*':
            UiActions.click(page.standard_clac.get_mult())
        elif value == '/':
            UiActions.click(page.standard_clac.get_divide())
        else:
            raise Exception('Invalid Input: ' + value)



    @staticmethod
    @allure.step('Calculate Random Numbers And Operators')
    def calculate_flow_random_numbers_and_operators():
        rand_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        rand_operator_list = ['+', '-', '*', '/']
        rand_number_size = ['1', '2', '3']
        first_num_char_long = random.choice(rand_number_size)  # first random number char size
        second_num_char_long = random.choice(rand_number_size)  # second random number char size
        first_rand_num = ''  # first random number
        second_rand_num = ''  # second random number
        for i in range(int(first_num_char_long)):
            first_rand_num += random.choice(rand_numbers)

        for i in range(int(second_num_char_long)):
            second_rand_num += random.choice(rand_numbers)

        rand_operator = random.choice(rand_operator_list)  # choose a random operator

        if second_rand_num == '0':    # make sure that second number will NOT BE equal to ZERO
            while second_rand_num == '0':
                for i in range(int(second_num_char_long)):
                    second_rand_num += random.choice(rand_numbers)


        output = first_rand_num + rand_operator + second_rand_num

        return output


    @staticmethod
    @allure.step('Get Calculator Result')
    def get_result_flow():
        result = page.standard_clac.get_result().text.replace("Display is", "").strip()
        return result

    @staticmethod
    @allure.step('Print The Result')
    def get_print_flow():
        result = page.standard_clac.get_result().text.replace("Display is", "").strip()
        print("The result to the random aritmatic actions are: " + result)
        # return result


    @staticmethod
    @allure.step('Clear Calculator Page')
    def clear_flow():
        UiActions.click(page.standard_clac.get_clear())
















