from django.test import SimpleTestCase
from django.urls import reverse,resolve
from Team.views import delqoditteam, showqoditteam,addqoditteam,delqoditteam,updqoditteam

class Testurls(SimpleTestCase):
    def test_list_urls_is_resolved(self):
        url=reverse('showteam')
        self.assertEqual(resolve(url).func,showqoditteam)

    def test_add_urls_is_resolved(self):
        url=reverse('addteam')
        self.assertEquals(resolve(url).func,addqoditteam)

    def test_delete_urls_is_resolved(self):
        url=reverse('deleteteam', args=[1988])
        self.assertEquals(resolve(url).func,delqoditteam)
    
    def test_update_urls_is_resolved(self):
        url=reverse('updateteam',args=[1988])
        self.assertEquals(resolve(url).func,updqoditteam)