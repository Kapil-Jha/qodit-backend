from django.test import SimpleTestCase
from django.urls import reverse,resolve
from Services.views import showqoditserv,addqoditserv,delqoditserv,updqoditserv

class Testurls(SimpleTestCase):
    def test_list_urls_is_resolved(self):
        url=reverse('showservices')
        self.assertEqual(resolve(url).func,showqoditserv)

    def test_add_urls_is_resolved(self):
        url=reverse('addservices')
        self.assertEquals(resolve(url).func,addqoditserv)

    def test_delete_urls_is_resolved(self):
        url=reverse('deleteservices', args=[1988])
        self.assertEquals(resolve(url).func,delqoditserv)
    
    def test_update_urls_is_resolved(self):
        url=reverse('updateservices',args=[1988])
        self.assertEquals(resolve(url).func,updqoditserv)