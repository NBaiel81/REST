from django.urls import path
from .views import *
urlpatterns =[
    path('users/',UserView.as_view()),
    path('book/',BookView.as_view()),
    path('author/',AuthorView.as_view())
]