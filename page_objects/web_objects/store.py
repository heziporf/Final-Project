from selenium.webdriver.common.by import By



accessories_button = (By.CSS_SELECTOR, "li[class='cat-item cat-item-28']")
men_button = (By.CSS_SELECTOR, "li[class='cat-item cat-item-39']")
women_button = (By.CSS_SELECTOR, "li[class='cat-item cat-item-47']")
select_dropdown = (By.XPATH, "//select[@name='orderby']")
list_of_items = (By.XPATH, "//h2[@class='woocommerce-loop-product__title']")
Anchor_Bracelet = (By.XPATH, "//h2[@class='woocommerce-loop-product__title']")[0]
add_to = (By.XPATH, "//*[text()='Add to cart']")
cart_items = (By.XPATH, "//div[@class='ast-cart-menu-wrap']")
search_button = (By.XPATH, "//div/input[@type='search']")


class Store:
    def __init__(self, driver):
        self.driver = driver

    def get_accessories_button(self):
        return self.driver.find_element(accessories_button[0], accessories_button[1])

    def get_men_button(self):
        return self.driver.find_element(men_button[0], men_button[1])

    def get_women_button(self):
        return self.driver.find_element(women_button[0], women_button[1])

    def get_select_dropdown(self):
        return self.driver.find_element(select_dropdown[0], select_dropdown[1])

    def get_list_of_items(self):
        return self.driver.find_elements(list_of_items[0], list_of_items[1])

    def get_Anchor_Bracelet(self):
        return self.driver.find_elements(Anchor_Bracelet[0], Anchor_Bracelet[1])

    def get_add_to(self):
        return self.driver.find_elements(add_to[0], add_to[1])

    def get_cart_items(self):
        return self.driver.find_element(cart_items[0], cart_items[1])

    def get_search_button(self):
        return self.driver.find_element(search_button[0], search_button[1])
