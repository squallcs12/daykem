'''
Created on Apr 20, 2014

@author: antipro
'''
from lettuce import step
from .selenium_shortcut import *
from lettuce_setup.short_dom import ShortDom
from lettuce_setup.utils import until_pass, until


@step(u'I should see a modal show up')
@until_pass
def i_should_see_a_modal_show_up(step):
    seen = False
    for modal in find_all(".modal"):
        if modal.is_displayed():
            seen = True
            break
    seen.should.be.true


@step(u'I should see on modal "([^"]*)"')
def i_should_see_on_modal(step, text):
    find(".modal").text.should.contain(text)


@step(u'I should see option on modal "([^"]*)"')
def i_should_see_option_on_modal(step, option_text):
    label = ShortDom.label(option_text)
    label.should.be.ok
    ShortDom.element_for_label(label).should.be.ok


@step(u'I should see button on modal "([^"]*)"')
def i_should_see_button_on_modal(step, button_text):
    ShortDom.button(button_text, ".modal").should.be.ok


@step(u'I should see checkbox on modal "([^"]*)"')
def i_should_see_checkbox_on_modal(step, checkbox_text):
    label = ShortDom.label(checkbox_text)
    label.should.be.ok
    checkbox = ShortDom.element_for_label(label)
    checkbox.should.be.ok
    checkbox.get_attribute("type").should.equal("checkbox")


@step(u'I click label on modal "([^"]*)"')
def i_click_label_on_modal(step, label_text):
    ShortDom.label(label_text, ".modal").click()


@step(u'I click button on modal "([^"]*)"')
def i_click_button_on_modal(step, button_text):
    ShortDom.button(button_text, ".modal").click()


@step(u'I fillin on modal field "([^"]*)" text "([^"]*)"')
def i_fillin_on_modal_field_by_value(step, label_text, value):
    label = ShortDom.label(label_text, ".modal")
    ShortDom.element_for_label(label).fill_in(value)


@step(u'I should see the popup notification "([^"]*)"')
def i_should_see_the_popup_notification(step, text):
    until(lambda: find("#popup-notification").is_displayed().should.be.true)
    find("#popup-notification .modal-body").text.should.contain(text)


@step(u'When I reload the page')
def when_i_reload_the_page(step):
    browser().refresh()


@step(u'I should see the form "([^"]*)"$')
def i_should_see_the_form_with_id(_, form_id):
    find("form#%s" % form_id)


@step(u'I should see the form "([^"]*)" fields:')
def i_should_see_the_form_fields(the_step, form_id):
    form = find("form#%s" % form_id)
    for field in the_step.hashes:
        label = ShortDom.label(field['name'], form)
        if label:  # normal field with label
            element = ShortDom.element_for_label(label)
            if element.tag_name == 'input':
                element.get_attribute('type').should.equal(field['type'])
            else:
                element.tag_name.should.equal(field['type'])
        else:
            field = ShortDom.element_by_tagname_and_text(field['type'], field['name'])
            field.should.be.ok


@step(u'I should see the button "([^"]*)" in state "([^"]*)"')
def i_should_see_the_button_group1_in_state_group2(_, button_label, state):
    button = ShortDom.button(button_label)
    button.should_has_class('btn-%s' % state)


@step(u'I fill in the form "([^"]*)" fields:')
def i_fill_in_the_form_group1_fields(the_step, form_id):
    form = find("form#%s" % form_id)
    for field in the_step.hashes:
        label = ShortDom.label(field['name'], form)
        element = ShortDom.element_for_label(label)
        element.fill_in(field['value'])


@step(u'I should see the form "([^"]*)" fields values:')
def i_should_see_the_form_fields_values(the_step, form_id):
    form = find("form#%s" % form_id)
    for field in the_step.hashes:
        label = ShortDom.label(field['name'], form)
        element = ShortDom.element_for_label(label)
        if element.text != field['value']:  # for html field like textarea, button
            element.get_attribute('value').should.equal(field['value'])


@step(u'the button "([^"]*)" done "([^"]*)"')
def the_button_group1_done_group2(_, button_label, state):
    button = ShortDom.button(button_label)
    until(lambda: button.has_class('btn-%s' % state).should_not.be.ok)


@step(u'I should see the "([^"]*)" table has rows:')
def i_should_see_the_table_has_rows(the_step, table_id):
    table = find("table#%s" % table_id)
    trs = table.find_all("tr")
    header_tr = trs[0]  # get all rows
    headers = [th.text for th in header_tr.find_all("th")]  # get header text

    for i in range(1, len(trs)):
        row = the_step.hashes[i - 1].copy()  # step row
        table_row = trs[i].find_all("td")  # row tds
        for j in range(0, len(headers)):  # for each header col
            table_row_col = table_row[j].text  # get the col text
            header_text = headers[j]  # get the header text
            if header_text in row:  # search for declared headers
                row[header_text].should.equal(table_row_col)  # compare
                del row[header_text]  # delete found
        row.should.be.empty  # all col found


@step(u'I should see the error "([^"]*)"')
def i_should_see_the_error_group1(_, error_text):
    error_texts = [e.text for e in find_all(".error")]
    error_texts.should.contain(error_text)


