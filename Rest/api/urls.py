from django.urls import path, include
from .views import *
from rest_framework import routers
router =routers.DefaultRouter()
router.register('order_set', OrderModelViewSet)
urlpatterns =[
    path('users/',UserView.as_view()),
    path('book/',BookView.as_view()),
    path('author/',AuthorView.as_view()),
    path('order/',OrderAPIView.as_view()),
    path('order/',include(router.urls)),
    path("order/<int:order_id>/",ModifyOrder.as_view()),
    path('my_orders/',MyOrderAPIView.as_view()),
    path('book_demo/<str:abbr>',BookDemoView.as_view())
]