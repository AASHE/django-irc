"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
from django.test import TestCase, Client


TEST_SERVER = 'localhost:8000'


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)


class ResourceUrlsTest(TestCase):

    def get_url_strings(self):
        import urls
        url_strings = list()
        for pattern in urls.urlpatterns:
            url_strings.append(str(pattern).split()[-1].translate(None, '^$>'))
        return url_strings

    def test_no_404(self):
        '''
        Tests that url is available.
        '''
        client = Client()
        bad_urls = []
        for url in self.get_url_strings():
            if not url:  # sometimes url is ''?
                continue
            try:
                resp = client.get('/'.join(('http:/', TEST_SERVER, url)))
                if resp.status_code == 200:
                    bad_urls.append(url)
            except:
                bad_urls.append(url)
        self.assertFalse(bad_urls,
                         msg='bad urls: {0}'.format(bad_urls))
