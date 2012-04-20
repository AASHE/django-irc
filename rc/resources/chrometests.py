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
LIVE_SERVER = 'www.aashe.org'

def get_url_strings(urls_module):
    '''This depends on urls.patterns, created by 'manage.py shell'.'''
    url_strings = list()
    for pattern in urls_module.urlpatterns:
	url_strings.append(pattern.regex.pattern.translate(None, '^$'))
    return url_strings


class ChromeTest(unittest.TestCase):

    def setUp(self, delay=1, compare_to_live=False):
        self.delay = delay
        self.compare_to_live = compare_to_live
	self.test_browser = webdriver.Chrome()
        self.live_browser = webdriver.Chrome() if compare_to_live else None
	self.addCleanup(self.tearDown)

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
            full_url = '/'.join(('http:/', TEST_SERVER, url))
	    self.test_browser.get(full_url)
            if self.compare_to_live:
                self.live_browser.get(full_url.replace(TEST_SERVER,
                                                       LIVE_SERVER))
            if self.delay:
                time.sleep(self.delay)
            else:
                _ = raw_input('press return to continue . . . ')
	    self.assertTrue(bool(
		self.test_browser.find_elements_by_id('resource_list')))

    def tearDown(self):
	self.test_browser.close()
        if self.compare_to_live:
            self.live_browser.close()

    def runTest(self, delay=1, compare_to_live=False):
	self.setUp(delay, compare_to_live)
        try:
            for app in ('education', 'operations', 'pae', 'policies',
                        'programs'):
                try:
                    self.test_urls(app)
                except Exception as e:
                    print e.message
                    pass
        except Exception as e:
            print e.message
        finally:
            self.tearDown()


if __name__ == '__main__':
    ChromeTest().runTest()
