from django.urls import path,include
from users import views as user_views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [  
    path('<str:username>/',user_views.Profile.as_view(),name="user_profile"),
    path('<str:username>/update-profile/',user_views.update_profile,name='update_profile'),
    path('<str:username>/change-password/', user_views.change_password, name='change_password'),
    path('<str:username>/delete-account/', user_views.delete_user, name='delete_user'),
    
]
