from django.urls import path
from . import views

app_name = 'giftlist'
urlpatterns = [
    path('', views.home, name='home'),
    path('groupresults/', views.groupResults, name='groupresults'),
    path('addgroup/', views.addGroup, name='addgroup'),
    path('grouplist/', views.groupLlist, name='grouplist'),
    path('memberlist/<User>', views.memberGiftList, name='membergiftlist')
]
