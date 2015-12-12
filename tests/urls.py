from django.conf.urls import url, include
from django.views.generic import RedirectView

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'books', views.BookViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
    url(r'^ehco/$', RedirectView.as_view(pattern_name='echo', permanent=False)),
    url(r'^echo/$', views.echo, name='echo'),
    url(r'^upload_file/$', views.upload_file),
]
