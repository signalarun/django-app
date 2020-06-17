from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:l_id>', views.listing, name='listing')
]