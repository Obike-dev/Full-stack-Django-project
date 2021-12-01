from django.urls import path
from shoes_app import views

app_name = 'shoes_app'

urlpatterns = [
    path('add-shoe/', views.AddShoe.as_view(), name='add_shoe'),
    path("<slug:slug>/", views.shoe_detail, name="shoe_detail"),
    path("<slug:slug>/edit-shoe/", views.edit_shoe, name="edit_shoe"),
    path('<slug:slug>/delete-shoe/', views.delete_shoe, name='delete_shoe'),

]
