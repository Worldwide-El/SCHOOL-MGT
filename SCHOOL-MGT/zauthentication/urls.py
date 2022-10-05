from django.urls import path
from .views import signup, logoutt



urlpatterns = [
    path('signup/', signup, name='signup'),
    path('logoutt/', logoutt, name='logoutt'),
]