from selenium.webdriver.common.by import By

main_headline = (By.XPATH, "//h1[@class='elementor-heading-title elementor-size-default']")

second_headline = (By.CSS_SELECTOR, "h3[class='elementor-heading-title elementor-size-default']")

atid_colledge_link = (By.CSS_SELECTOR, "a[href='https://atidcollege.co.il/']")

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def get_main_headline(self):
        return self.driver.find_element(main_headline[0], main_headline[1])

    def get_second_headline(self):
        return self.driver.find_element(second_headline[0], second_headline[1])

    def get_atid_colledge_link(self):
        return self.driver.find_element(atid_colledge_link[0], atid_colledge_link[1])

