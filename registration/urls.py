from django.urls import path
from .views import SingUpView, ProfileUpdate, userUpdate

urlpatterns = [
    path('signup/', SingUpView.as_view(), name="signup"),
    path('profile/', ProfileUpdate.as_view(), name="profile"),
    path('profile/data/', userUpdate.as_view(), name="profile_data"),
]