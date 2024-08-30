from django.urls import path
from .views import *

urlpatterns = [
    path('person/create/', create_person ),
    path('person/list/', list_persons ),
    path('person/update/<pk>/', update_person ),
    path('person/delete/<pk>/', delete_person ),
    path('person/retrieve/<pk>/', retrieve_persons),
]


