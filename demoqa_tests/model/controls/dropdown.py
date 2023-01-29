from selene import command, have
from selene.support.shared import browser


def select(selector, by_text):
    browser.element(selector).perform(command.js.scroll_into_view).click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text(by_text)
    ).perform(command.js.click)
