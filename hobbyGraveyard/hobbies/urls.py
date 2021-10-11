from django.urls import path
from . import views

urlpatterns=[
    path('',views.index,name="list"),
    path('update_task/<str:pk>/',views.updateHobby, name = "update_hobby"),
    path('delete/<str:pk>/',views.deleteHobby, name='delete')
]