from django.urls import path, include


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('regsiter/', RegisterView.as_view(), name='register'),
]
