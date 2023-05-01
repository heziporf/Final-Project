from selenium.webdriver.common.by import By
home_button = (By.XPATH, "//li[@id='menu-item-381']")
store_button = (By.XPATH, "//li[@id='menu-item-45']")
men_button = (By.XPATH, "//li[@id='menu-item-266']")
women_button = (By.XPATH, "//li[@id='menu-item-267']")
accessories = (By.XPATH, "//li[@id='menu-item-671']")
about = (By.XPATH, "//li[@id='menu-item-828']")
contact = (By.XPATH, "//li[@id='menu-item-829']")
home_button_image = (By.XPATH, "//img[@width='160' and @height='63']")[0]
search = (By.XPATH, "//div[@class='ast-search-menu-icon slide-search']")
search_after_click = (By.XPATH, "//a[@class='slide-search astra-search-icon']")
search_input = (By.XPATH, "//input[@type='search']")
price = (By.XPATH, "//span/span[@class='woocommerce-Price-amount amount']")[0]
cart_items = (By.XPATH, "//div[@class='ast-cart-menu-wrap']")



class Header:
    def __init__(self, driver):
        self.driver = driver

    def get_home_button(self):
        return self.driver.find_element(home_button[0], home_button[1])

    def get_store_button(self):
        return self.driver.find_element(store_button[0], store_button[1])

    def get_men_button(self):
        return self.driver.find_element(men_button[0], men_button[1])

    def get_women_button(self):
        return self.driver.find_element(women_button[0], women_button[1])

    def get_accessories(self):
        return self.driver.find_element(accessories[0], accessories[1])

    def get_about(self):
        return self.driver.find_element(about[0], about[1])

    def get_contact(self):
        return self.driver.find_element(contact[0], contact[1])

    def get_home_button_image(self):
        return self.driver.find_element(home_button_image[0], home_button_image[1])

    def get_search(self):
        return self.driver.find_element(search[0], search[1])

    def get_search_after_click(self):
        return self.driver.find_element(search_after_click[0], search_after_click[1])

    def get_search_input(self):
        return self.driver.find_element(search_input[0], search_input[1])

    def get_price(self):
        return self.driver.find_element(price[0], price[1])

    def get_cart_items(self):
        return self.driver.find_element(cart_items[0], cart_items[1])