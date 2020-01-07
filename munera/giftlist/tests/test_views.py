from django.test import RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from giftlist.views import home, groupResults
from mixer.backend.django import mixer
import pytest

pytestmark = pytest.mark.django_db

@pytest.mark.django_db
class TestViews:
    pytestmark = pytest.mark.django_db
    
    def test_home_authenticated(self):
        path = reverse('giftlist:home')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = home(request)
        assert response.status_code == 200

    def test_groupresults_view(self):
        path = reverse('giftlist:groupresults')
        request = RequestFactory().get(path)
        request.user = mixer.blend(User)

        response = groupResults(request)
        assert response.status_code == 200
