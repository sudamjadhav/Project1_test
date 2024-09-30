from django.urls import path
from .views import register, update_user, CustomLoginView, CustomLogoutView


urlpatterns = [
    path('register/', register, name='register'),
    path('update-user/', update_user, name='update_user'),

    path('login/', CustomLoginView.as_view(), name='login' ),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    


]