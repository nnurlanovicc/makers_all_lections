from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegistrationView.as_view()),
    path('activate/', ActivationView.as_view()),
    path('login/', loginView.as_view()),
    path('logout/', LogoutView.as_view()),


]

