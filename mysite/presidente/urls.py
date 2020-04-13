from django.urls import path, re_path

from .import views

app_name = 'presidente'
urlpatterns = [
    path('', views.index, name='index'),
    path('card/<int:id>/', views.detail),    
    path('cards/', views.index, name="cards-all"),
    path('cards-by-type/', views.cards_by_type, name="cards-by-type")
]
