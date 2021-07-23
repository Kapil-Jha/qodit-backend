from django.test import SimpleTestCase
from django.urls import reverse,resolve
from HeroBox.views import showqodithero,addqoditero,delqodithero,updqoditero

class Testurls(SimpleTestCase):
    def test_list_urls_is_resolved(self):
        url=reverse('showherobox')
        self.assertEqual(resolve(url).func,showqodithero)

    def test_add_urls_is_resolved(self):
        url=reverse('addherobox')
        self.assertEquals(resolve(url).func,addqoditero)

    def test_delete_urls_is_resolved(self):
        url=reverse('deleteherobox', args=[1988])
        self.assertEquals(resolve(url).func,delqodithero)
    
    def test_update_urls_is_resolved(self):
        url=reverse('updateherobox',args=[1988])
        self.assertEquals(resolve(url).func,updqoditero)