from selene import have
from selene.support.shared import browser


def select(selector, by_text):
    browser.all(selector).element_by(have.value(by_text)).element('..').click()
