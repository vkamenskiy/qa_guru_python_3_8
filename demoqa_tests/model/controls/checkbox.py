from selene import have
from selene.support.shared import browser


def select(selector, *, by_texts: tuple):
    for by_text in by_texts:
        browser.all(selector).element_by(have.text(by_text)).click()
