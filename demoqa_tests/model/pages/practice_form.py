from selene import have, command
from selene.support.shared import browser

from demoqa_tests.model.controls import (
    dropdown,
    checkbox,
    radio,
    datepicker,
    multiselect,
)
from demoqa_tests.utils import resource


def given_opened():
    browser.open('/automation-practice-form')
    browser.execute_script(
        'document.querySelector(".body-height").style.transform = "scale(.5)"'
    )
    ads = browser.all('[id^=google_ads][id$=container__]')
    ads.with_(timeout=10).should(have.size_greater_than_or_equal(3)).perform(
        command.js.remove
    )

    if ads.with_(timeout=2).wait_until(have.size_greater_than_or_equal(2)):
        ads.perform(command.js.remove)


def select_state(value):
    dropdown.select('#state', by_text=value)


def select_city(value):
    dropdown.select('#city', by_text=value)


def select_hobbies(*texts: str):
    checkbox.select('[for^=hobbies-checkbox]', by_texts=texts)


def select_gender(value):
    radio.select('[name=gender]', by_text=value)


def select_subjects(value):
    multiselect.select('#subjectsInput', by_text=value)


def select_date_of_birth(day, month, year):
    datepicker.select('#dateOfBirthInput', day, month, year)


def submit():
    browser.element('#submit').perform(command.js.click)


def fill_name(value):
    browser.element('#firstName').type(value)


def fill_last_name(value):
    browser.element('#lastName').type(value)


def fill_email(value):
    browser.element('#userEmail').type(value)


def fill_mobile_number(value):
    browser.element('#userNumber').type(value)


def fill_current_address(value):
    browser.element('#currentAddress').type(value)


def upload_picture(file):
    browser.element('#uploadPicture').send_keys(resource.abs_path(file))


def assert_submitted(*data):
    browser.element('.table').all('td:nth-of-type(2)').should(have.texts(data))
