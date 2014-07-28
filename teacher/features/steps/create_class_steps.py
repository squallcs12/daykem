# -*- coding: utf-8 -*-
"""
Created on 27/07/2014

@author: antipro
"""
__author__ = 'antipro'

from lettuce_setup.function import *


@step(u'I was a logged in "([^"]*)" user')
def i_was_a_logged_in_group_user(_, account_type):
    i_was_a_registered_in_user(_)
    world.user.account_type = account_type
    world.user.save()
    i_first_login_into_my_account(_)


@step(u'I go to "([^"]*)" page')
def i_go_to_group1_page(_, page_name):
    visit_by_view_name(page_name)


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
