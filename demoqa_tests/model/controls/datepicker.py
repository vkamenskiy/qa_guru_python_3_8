from selene.support.shared import browser


def select(selector, day, month, year):
    browser.element(selector).click()
    browser.element(f'.react-datepicker__year-select [value="{year}"]').click()
    browser.element(f'.react-datepicker__month-select [value="{month}"]').click()
    browser.element(f'.react-datepicker__day--0{day}').click()
