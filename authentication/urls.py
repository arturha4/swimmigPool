from django.urls import path
from authentication.views import UserRegisterView, UserLoginView, user_logout

urlpatterns = [
    path('registration/', UserRegisterView.as_view(), name='registration'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', user_logout, name='logout'),
]
