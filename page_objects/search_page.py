from selenium.webdriver.common.by import By


class SearchPage:

    # Locators
    SEARCH_BAR = (By.ID, 'searchBar')
    RESULTS = (By.CSS_SELECTOR, '#productList li a h2')

    def __init__(self, driver):
        self.driver = driver

    def filter_books(self, search_text):
        element = self.driver.find_element(*self.SEARCH_BAR)
        element.send_keys(search_text)

    def verify_visible_books_by_title(self, expected_title):
        elements = self.driver.find_elements(*self.RESULTS)
        for element in elements:
            if expected_title in element.text:
                return True
        return False
