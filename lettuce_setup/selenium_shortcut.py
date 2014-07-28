'''
Created on Apr 10, 2014

@author: eastagile
'''
from lettuce import world, after
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement


def browser():
    '''
    @return: selenium.webdriver.Firefox
    '''
    if not hasattr(world, 'browser'):
        world.browser = webdriver.Firefox()
        world.browser.maximize_window()
        world.browser.implicitly_wait(3)
    return world.browser


@after.each_scenario
def close_browser(scenario):
    if hasattr(world, 'browser'):
        world.browser.quit()
        del world.browser


def find_all(selector):
    return browser().find_elements_by_css_selector(selector)


def find(selector):
    return browser().find_element_by_css_selector(selector)


def xpath(selector):
    return browser().find_element_by_xpath(selector)


WebElement.find = WebElement.find_element_by_css_selector
WebElement.find_all = WebElement.find_elements_by_css_selector
WebElement.xpath = WebElement.find_element_by_xpath


def select_by_text(self, option_text):
    self.xpath("./option[text()='%s']" % option_text).click()


WebElement.select_by_text = select_by_text


def select_by_value(self, option_value):
    self.xpath("./option[@value='%s']" % option_value).click()


WebElement.select_by_value = select_by_value


def has_class(self, class_name):
    return class_name in self.get_attribute('class').split(' ')


WebElement.has_class = has_class


def should_has_class(self, class_name):
    return self.has_class(class_name).should.be.ok


WebElement.should_has_class = should_has_class


def should_be_temp_link(self):
    self.tag_name.should.equal('a')
    self.get_attribute('href').should.equal(browser().current_url + '#')


WebElement.should_be_temp_link = should_be_temp_link


def fill_in(self, value):
    assert isinstance(self, WebElement)
    if self.tag_name == 'textarea':
        if self.value_of_css_property('display').lower() == 'none':
            try:
                cke_container = self.xpath('../div')
                if cke_container.has_class('cke'):
                    browser().switch_to.frame(cke_container.find(".cke_wysiwyg_frame"))
                    find(".cke_editable").send_keys(value)
                    browser().switch_to.default_content()
            except NoSuchElementException:
                pass
    elif self.tag_name == 'select':
        if value:
            self.select_by_text(value)
        else:
            self.select_by_value(value)
    elif self.tag_name == 'input':
        self.clear()
        self.send_keys(value)


WebElement.fill_in = fill_in
