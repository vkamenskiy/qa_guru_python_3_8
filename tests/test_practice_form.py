from demoqa_tests.model.pages import practice_form


def test_successful_submit_student_registration_form():
    practice_form.given_opened()

    # WHEN
    practice_form.fill_name('Vladislav')
    practice_form.fill_last_name('Kamenskiy')
    practice_form.fill_email('dje.fry@mail.ru')
    practice_form.select_gender('Male')
    practice_form.fill_mobile_number('9162754427')
    practice_form.select_date_of_birth(19, 8, 1994)
    practice_form.select_subjects('English')
    practice_form.select_hobbies('Sports')
    practice_form.select_hobbies('Music')
    practice_form.upload_picture('test_pictures.webp')
    practice_form.current_address('Novotushinskiy proezd 8')
    practice_form.select_state('Haryana')
    practice_form.select_city('Panipat')
    practice_form.submit()

    # THEN
    practice_form.validation(
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
