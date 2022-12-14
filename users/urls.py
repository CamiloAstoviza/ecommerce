from django.urls import path
from users.views import login_request,register_request
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/',login_request,name='login'),
    path('register/',register_request,name='register'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name='logout')

]