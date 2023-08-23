from django.urls import path, include

from account.views import RegisterView

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('regsiter/', RegisterView.as_view(), name='register'),
]
