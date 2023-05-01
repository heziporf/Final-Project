from selenium.webdriver.common.by import By
search_results = (By.XPATH, "//h1[@class='page-title ast-archive-title']")
search_results_in_store_search = (By.XPATH, "//h2[@class='woocommerce-loop-product__title']")



class Search:
    def __init__(self, driver):
        self.driver = driver

    def get_search_results(self):
        return self.driver.find_element(search_results[0], search_results[1])

    def search_results_in_store_search(self):
        return self.driver.find_elements(search_results_in_store_search[0], search_results_in_store_search[1])