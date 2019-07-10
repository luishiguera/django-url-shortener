from django.urls import path
from .views import CreateShorten, LinkPage, RedirectLink

app_name = 'core'
urlpatterns = [
    path('', CreateShorten.as_view(), name='home'),
    path('<int:pk>/', LinkPage.as_view(), name='detail'),
    path('<str:code>/', RedirectLink.as_view(), name='redirect'),
]