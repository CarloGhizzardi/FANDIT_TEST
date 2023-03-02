from django.urls import path
from users.API.views import RegisterUserView

urlpatterns= {
    path('auth/register', RegisterUserView.as_view()),

}