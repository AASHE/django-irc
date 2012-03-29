'''
Tests that drive Chrome.  They're interactive insofar as they'll pop
up a browser and load pages into it.

There's a dependency on urls.patterns, so here's how I've been running
this:

  $ manage.py shell
  >>> from rc.resources.chrometests import ChromeTest
  >>> ChromeTest.runTest()

Must be a way to pass a script to Django via manage.py . . .

Other dependencies include an installed Chrome, and the selenium
package.
'''
import time
import unittest

from selenium import webdriver


TEST_SERVER = 'localhost:8000'

def get_url_strings():
    '''This depends on urls.patterns, created by 'manage.py shell'.'''
    import urls
    url_strings = list()
    for pattern in urls.urlpatterns:
	url_strings.append(str(pattern).split()[-1].translate(None, '^$>'))
    return url_strings


class ChromeTest(unittest.TestCase):

    def setUp(self):
	self.browser = webdriver.Chrome()
	self.addCleanup(self.tearDown)
    
    def test_resource_list_there(self):
	'''
	Each resource item list page has a div with id 'resource_list'.
	This test just loads a URL and looks for the resource_list element.
	It's a quick test to see if the page is loading.
	'''
	for url in get_url_strings():
	    self.browser.get('/'.join(('http:/', TEST_SERVER, url)))
	    time.sleep(self.delay)
	    self.assertTrue(bool(
		self.browser.find_elements_by_id('resource_list')))

    def tearDown(self):
	self.browser.close()
            
    def runTest(self, delay=1):
	self.delay=delay
	self.setUp()
	try:
	    self.test_resource_list_there()
	finally:
	    self.tearDown()




