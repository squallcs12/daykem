# -*- coding: utf-8 -*-
"""
Created on 26/07/2014

@author: antipro
"""
__author__ = 'antipro'

from lettuce_setup.function import *


@step(u'I should see the setup account form')
def i_should_see_the_setup_account_form(_):
    find("#accounts_setup")


@step(u'my account should be set to "([^"]*)" type')
def my_account_should_be_set_to_group1_type(_, account_type):
    refresh_user = User.objects.get(pk=world.user.id)
    refresh_user.account_type.should.equal(account_type)
