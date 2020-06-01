from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import unittest

geckodriver_path = r'C:\Users\Romas\geckodriver\geckodriver.exe'

class NewVisitorTest(StaticLiveServerTestCase):
    def setUp(self):
        self.fail('URLs in this class require login. Please remove @login_required in views.py :)')
        self.browser = webdriver.Firefox(executable_path=geckodriver_path)

    def tearDown(self):
        self.browser.quit()

    def item_in_list(self, item, list):
        ul = self.browser.find_element_by_id(list)
        list_items = ul.find_elements_by_tag_name('li')
        return (item in [li.text for li in list_items])

    def check_item_in_list(self, item, list):
        self.assertTrue(self.item_in_list(item, list))

    def check_item_not_in_list(self, item, list):
        self.assertFalse(self.item_in_list(item, list))

    def click_button(self, id):
        button = self.browser.find_element_by_id(id)
        button.click()
        time.sleep(2)

    def populate_field(self, id, text):
        inputbox = self.browser.find_element_by_id(id)
        inputbox.send_keys(text)

    def hit_enter(self):
        inputbox = self.browser.find_element_by_id('id_title')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

    def check_header_exists(self, header):
        headers = self.browser.find_elements_by_class_name('cv-title')
        self.assertIn(header, [h.text for h in headers])

    def delete_item_in_list(self, item, list):
        ul = self.browser.find_element_by_id(list)
        list_items = ul.find_elements_by_tag_name('li')
        for i in list_items:
            if i.text == item:
                i.find_element_by_tag_name('a').click()
                break
        time.sleep(2)

    def check_add_to_list_then_retrieve_then_delete(self, header, add_button, curr_list, data):
        # Open homepage
        self.browser.get(self.live_server_url + '/cv/')

        # Check the page title
        self.assertIn('Rmlds | Personal Website | University Coursework', self.browser.title)

        # Check the header exists
        self.check_header_exists(header)

        # We click a button to add a new item, new page opens up
        self.click_button(add_button)

        # We fill out the form
        for field in data[0]:
            self.populate_field('id_' + field, data[0][field])

        # When we hit enter, the page redirects, and now it has
        # the previously added item in the list
        self.hit_enter()

        self.check_item_in_list(data[0]['title'], curr_list)

        # We click a button to add another item, new page opens up
        self.click_button(add_button)

        # We fill out the form again
        for field in data[1]:
            self.populate_field('id_' + field, data[1][field])
        self.hit_enter()

        # The page redirects, and now shows both items in the list
        self.check_item_in_list(data[0]['title'], curr_list)
        self.check_item_in_list(data[1]['title'], curr_list)

        # We click delete next to the first item, page reloads
        self.delete_item_in_list(data[0]['title'], curr_list)

        # The item is deleted and no longer in the list
        self.check_item_not_in_list(data[0]['title'], curr_list)
        self.check_item_in_list(data[1]['title'], curr_list)

    def test_can_add_to_skill_list_then_retrieve_then_delete(self):

        data=[{"title": "Awesome1",}, {"title": "Awesome2",}]
        
        self.check_add_to_list_then_retrieve_then_delete(
            'Skills',
            'add-skill',
            'skill-list',
            data
        )

    def test_can_add_to_education_list_then_retrieve_then_delete(self):

        data=[
            {"title": "TheEducation1", "date": "2018", "description": "e1"}, 
            {"title": "TheEducation2", "date": "2020", "description": "e2"}]
        
        self.check_add_to_list_then_retrieve_then_delete(
            'Education',
            'add-education',
            'education-list',
            data
        )

    def test_can_add_to_achievement_list_then_retrieve_then_delete(self):

        data=[
            {"title": "Achievement1", "date": "2015"},
            {"title": "Achievement2", "date": "2019"}]
        
        self.check_add_to_list_then_retrieve_then_delete(
            'Achievements',
            'add-achievement',
            'achievement-list',
            data
        )

    def test_can_add_to_course_list_then_retrieve_then_delete(self):

        data=[{"title": "BestCourse1",}, {"title": "BestCourse2",}]
        
        self.check_add_to_list_then_retrieve_then_delete(
            'Courses',
            'add-course',
            'course-list',
            data
        )
