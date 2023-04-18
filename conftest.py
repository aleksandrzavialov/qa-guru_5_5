import pytest
from selene.support.shared import browser
from selene import be, have, command


@pytest.fixture(scope='session')
def browser_actions():
    browser.config.base_url = 'https://demoqa.com/automation-practice-form'
    browser.open('/')
    browser.driver.set_window_size(1920, 1080)
    # Remove banner
    if browser.element('#fixedban').wait_until(be.visible):
        browser.element('#fixedban').perform(command.js.remove)
    browser.element('footer span').should(have.text('© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED'))
    browser.element('footer').perform(command.js.remove)
    yield browser
    browser.close()
