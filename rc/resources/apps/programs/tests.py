import unittest

from rc.resources.apps.programs import urls

class UrlsTestCase(unittest.TestCase):

    def test_all_urls_named(self):
        unnamed_urls = []
        for url in urls.urlpatterns:
            if not url.name:
                unnamed_urls.append(url.regex.pattern)
        self.assertFalse(unnamed_urls,
                         msg='unnamed url(s): {0}'.format(unnamed_urls))
