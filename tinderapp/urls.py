from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('current_user', views.CurrentUserView.as_view()),
    path('toggle_available', views.ToggleAvailability.as_view()),
    path('get_available_users', views.GetAvailableUsers.as_view())
]
