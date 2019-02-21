from selenium import webdriver
from selenium.webdriver.common.keys import keys
import unittest

browser = webdriver.Firefox()
browser.get('http://localhost:8000')

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_post(self):
        self.browser.get('http://localhost:8000')



    # I am on the website. I notice the name "Cool Blog" in the title of the siteself.
        self.assertIn('Cool Blog', header_text)


    # There is a 'title' section, and a 'content' section; where I am allowed to name  a post
        titlebox = self.browser.find_element_by_id('id_new_post_title')
        inputbox = self.browser.find_element_by_id('id_new_post_content')

    # I write "My bad day" in the title of the postself. I hit enter,
        titlebox.sendKeys("My Bad Day")
    # I then write "My day was bad because I was hit by a truck" in the content section of the site.
        inputbox.sendKeys("My day was bad because I was hit by a truck")

    # I hit a button called "Save", which adds the post; title and all, to the bottom of the page
        submitbutton = self.browser.find_element_by_id('submit_button')
    # The input box for the "title" and "content" are now blank.

    # I refresh the page, the content is still thereself.

if __name__ == '__main__':
    unittest.main(warnings='ignore')
