import pytest
from selene import browser


@pytest.fixture(scope='function')
def browser_window_size():
    browser.open('https://startpage.com')
    browser.driver.set_window_size(1280, 800)
    yield
    browser.quit()
