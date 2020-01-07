from django.urls import reverse, resolve

class TestUrls:

    def test_home_url(self):
        path = reverse('giftlist:home')
        assert resolve(path).view_name == 'giftlist:home'

    def test_groupresults_url(self):
        path = reverse('giftlist:groupresults')
        assert resolve(path).view_name == 'giftlist:groupresults'

    def test_grouplist_url(self):
        path = reverse('giftlist:grouplist')
        assert resolve(path).view_name == 'giftlist:grouplist'

    def test_memberlist_url(self):
        path = reverse('giftlist:membergiftlist', kwargs={'User':1})
        assert resolve(path).view_name == 'giftlist:membergiftlist'
