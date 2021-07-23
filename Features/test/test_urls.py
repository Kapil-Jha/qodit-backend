from django.test import SimpleTestCase
from django.urls import reverse,resolve
from Features.views import showqoditfeat,addqoditfeat,delqoditfeat,updqoditfeat

class Testurls(SimpleTestCase):
    def test_list_urls_is_resolved(self):
        url=reverse('showfeatures')
        self.assertEqual(resolve(url).func,showqoditfeat)

    def test_add_urls_is_resolved(self):
        url=reverse('addfeatures')
        self.assertEquals(resolve(url).func,addqoditfeat)

    def test_delete_urls_is_resolved(self):
        url=reverse('deletefeatures', args=[1988])
        self.assertEquals(resolve(url).func,delqoditfeat)
    
    def test_update_urls_is_resolved(self):
        url=reverse('updatefeatures',args=[1988])
        self.assertEquals(resolve(url).func,updqoditfeat)