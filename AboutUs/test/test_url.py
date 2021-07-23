from django.test import SimpleTestCase
from django.urls import reverse,resolve
from AboutUs.views import showqoditus,addqoditus,delqoditus,updqoditus

class Testurls(SimpleTestCase):
    def test_list_urls_is_resolved(self):
        url=reverse('showus')
        self.assertEqual(resolve(url).func,showqoditus)

    def test_add_urls_is_resolved(self):
        url=reverse('addus')
        self.assertEquals(resolve(url).func,addqoditus)

    def test_delete_urls_is_resolved(self):
        url=reverse('deleteus', args=[1988])
        self.assertEquals(resolve(url).func,delqoditus)
    
    def test_update_urls_is_resolved(self):
        url=reverse('updateus',args=[1988])
        self.assertEquals(resolve(url).func,updqoditus)

