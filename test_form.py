from selene.support.shared import browser
from selene import be, have, command
import os


def test_form_filling(browser_actions):
    browser.element('#firstName').should(be.blank).type('Ivan')
    browser.element('#lastName').should(be.blank).type('Petrov')
    browser.element('#userEmail').should(be.blank).type('ivanpetrov@mail.ru')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').should(be.blank).type('8999999999')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select [value="1989"]').click()
    browser.element('.react-datepicker__month-select [value="10"]').click()
    browser.element('.react-datepicker__day--019').click()
    browser.element('#subjectsInput').should(be.blank).type('Maths').press_tab()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + "\\images\\Owlet.jpg")
    browser.element('#currentAddress').should(be.blank).type('Pushkina Street, Kolotushkina house')
    browser.element('#state').perform(command.js.scroll_into_view).click()
    browser.element('#react-select-3-option-1').click()
    browser.element('#city').should(be.clickable).click()
    browser.element('#react-select-4-option-2').click()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all(' td:nth-of-type(1)').should(have.exact_texts('Student Name', 'Student Email', 'Gender', 'Mobile',
                                                              'Date of Birth', 'Subjects', 'Hobbies', 'Picture',
                                                              'Address', 'State and City'))
    browser.all(' td:nth-of-type(2)').should(have.exact_texts('Ivan Petrov', 'ivanpetrov@mail.ru', 'Male', '8999999999',
                                                              '19 November,1989', 'Maths', 'Reading', 'Owlet.jpg',
                                                              'Pushkina Street, Kolotushkina house',
                                                              'Uttar Pradesh Merrut'))
    browser.element('#closeLargeModal').should(be.clickable)
