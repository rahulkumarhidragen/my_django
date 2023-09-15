from django import urls
from . import views

urlpatterns = [
    urls.path('', views.index, name='index'),
    urls.path('complete_registration/', views.complete_registration, name='complete_registration'),
    urls.path('view_user/', views.view_user, name='view_user'),
]