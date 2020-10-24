from django.urls import include, path

urlpatterns = [
    path('', include('tinderapp.urls')),
    path('users/', include('tinderapp.urls')),
    path('auth/', include('rest_auth.urls')),
    path('auth/registration/', include('rest_auth.registration.urls')),
]
