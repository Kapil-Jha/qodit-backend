from django.test import SimpleTestCase
from django.urls import reverse,resolve
from Testimonial.views import showqodittesti,addqodittesti,delqodittesti,updqodittesti

class Testurls(SimpleTestCase):
    def test_list_urls_is_resolved(self):
        url=reverse('showtestimonial')
        self.assertEqual(resolve(url).func,showqodittesti)

    def test_add_urls_is_resolved(self):
        url=reverse('addtestimonial')
        self.assertEquals(resolve(url).func,addqodittesti)

    def test_delete_urls_is_resolved(self):
        url=reverse('deletetestimonial', args=[1988])
        self.assertEquals(resolve(url).func,delqodittesti)
    
    def test_update_urls_is_resolved(self):
        url=reverse('updatetestimonial',args=[1988])
        self.assertEquals(resolve(url).func,updqodittesti)