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

def get_url_strings(urls_module):
    '''This depends on urls.patterns, created by 'manage.py shell'.'''
    url_strings = list()
    for pattern in urls_module.urlpatterns:
	url_strings.append(str(pattern).split()[-1].translate(None, '^$>'))
    return url_strings


class ChromeTest(unittest.TestCase):

    def setUp(self):
	self.browser = webdriver.Chrome()
	self.addCleanup(self.tearDown)

    def test_education_urls(self):
        self.test_urls('education')

    def test_operations_urls(self):
        self.test_urls('operations')

    def test_urls(self, app_name):
        app = __import__('rc.resources.apps.' + app_name, globals(), locals(),
                         ['urls'])
        self.test_resource_list_there(app.urls)

    def test_resource_list_there(self, urls_module):
	'''
	Each resource item list page has a div with id 'resource_list'.
	This test just loads a URL and looks for the resource_list element.
	It's a quick test to see if the page is loading.
	'''
	for url in get_url_strings(urls_module):
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
            for test in (self.test_education_urls,
                         self.test_operations_urls):
                try:
                    test()
                except Exception as e:
                    print e.message
                    pass
        except Exception as e:
            print e.message
        finally:
            self.tearDown()


if __name__ == '__main__':
    ChromeTest().runTest()
