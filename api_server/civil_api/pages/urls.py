# pages/urls.py
from django.conf.urls import url

from .views import homePageView, testView

urlpatterns = [
    url('^test', testView, name='test'),
    url('', homePageView, name='home')
]
