from selene.support.shared import browser
from selene import have, command
import os
import tests


def test_successful_submit_student_registration_form():
    browser.open('/automation-practice-form')
    ads = browser.all('[id^=google_ads][id$=container__]')
    ads.with_(timeout=10).should(have.size_greater_than_or_equal(3)).perform(
        command.js.remove
    )

    if ads.with_(timeout=2).wait_until(have.size_greater_than_or_equal(2)):
        ads.perform(command.js.remove)

    # WHEN
    browser.element('#firstName').type('Vladislav')
    browser.element('#lastName').type('Kamenskiy')
    browser.element('#userEmail').type('dje.fry@mail.ru')
    browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()
    browser.element('#userNumber').type('9162754427')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select [value="1994"]').click()
    browser.element('.react-datepicker__month-select [value="8"]').click()
    browser.element(f'.react-datepicker__day--0{19}').click()

    browser.element('#subjectsInput').type('en')
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text("English")
    ).click()

    browser.all('[for^=hobbies-checkbox]').element_by(have.text('Sports')).element(
        '..'
    ).click()
    browser.all('[for^=hobbies-checkbox]').element_by(have.text('Music')).element(
        '..'
    ).click()

    browser.element('#uploadPicture').send_keys(
        os.path.abspath(
            os.path.join(
                os.path.dirname(tests.__file__), '../resources/test_pictures.webp'
            )
        )
    )

    browser.element('#currentAddress').type('Novotushinskiy proezd 8')

    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('Haryana')
    ).click()
    browser.element('#city').click()
    browser.all('[id^=react-select][id*=option]').element_by(
        have.exact_text('Panipat')
    ).perform(command.js.click)

    browser.element('#submit').perform(command.js.click)

    # THEN
    browser.element('.table').all('td:nth-of-type(2)').should(
        have.texts(
            'Vladislav Kamenskiy',
            'dje.fry@mail.ru',
            'Male',
            '9162754427',
            '19 September,1994',
            'English',
            'Sports, Music',
            'test_pictures.webp',
            'Novotushinskiy proezd 8',
            'Haryana Panipat',
        )
    )

def test_commit