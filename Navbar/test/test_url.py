from django.test import SimpleTestCase
from django.urls import reverse,resolve
from Navbar.views import showqodit,addqodit,delqodit,updqodit

class Testurls(SimpleTestCase):
    def test_list_urls_is_resolved(self):
        url=reverse('show')
        self.assertEqual(resolve(url).func,showqodit)

    def test_add_urls_is_resolved(self):
        url=reverse('add')
        self.assertEquals(resolve(url).func,addqodit)

    def test_delete_urls_is_resolved(self):
        url=reverse('delete', args=[1988])
        self.assertEquals(resolve(url).func,delqodit)
    
    def test_update_urls_is_resolved(self):
        url=reverse('update',args=[1988])
        self.assertEquals(resolve(url).func,updqodit)

