from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('about/', views.about, name='about'),
    path('financial_guide/', views.financial_guide, name='fin_guide'),  # усі статті
    path('<slug:category>', views.category, name='category'),  # статті певної категорії
    path('article/<int:pk>', views.article, name='article'),
    # path('article/', views.main_page, name='article_create'),  # форма щоб запостити статтю
]