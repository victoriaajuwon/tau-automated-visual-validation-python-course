from selenium.webdriver.common.by import By

from tests.conftest import validate_window
from tests.conftest import validate_element
from tests.conftest import validate_frame


def test_full_page_screenshot(driver, eyes):
    validate_window(driver, eyes, tag=None)


def test_book_by_region(driver, eyes):
    element = driver.find_element(By.ID, 'pid3')
    validate_element(driver, eyes, element, tag=None)


def test_element_in_frame(driver, eyes):
    frame = driver.find_element(By.TAG_NAME, 'iframe')
    validate_frame(driver, eyes, frame, (By.ID, 'tinymce'), tag=None)
