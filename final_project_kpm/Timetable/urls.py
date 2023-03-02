from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name = "index"),
    path('login', views.login , name = "login"),
    path('signup', views.signup, name = "signup"),
    path('homepage', views.homepage , name = "homepage"),
    path('searchSubject', views.searchSubject , name = "searchSubject"),
    path('list_subject', views.list_subject , name = "list_subject"),
    path('assignment', views.assignment , name = "assignment"),
    path('list_assignment', views.list_assignment , name = "list_assignment"),
    path('update_assignment/<id>', views.update_assignment , name = "update_assignment"),
    path('update_assignment/save_update_assignment/<id>', views.save_update_assignment , name = "save_update_assignment"),
    path('delete_assignment/<id>', views.delete_assignment, name='delete_assignment'),
    
]