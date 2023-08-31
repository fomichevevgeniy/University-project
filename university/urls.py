from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('news/', news, name='news'),
    path('study/', study, name='study'),
    path('for-students/', forstudents, name='forstudents'),
    path('contact/', contact, name='contact'),
    path('submission/', submission, name='submission'),
    path('document/', document, name='document'),
    path('for_enroll/', for_enroll, name='for_enroll'),
    path('news_detail/<int:news_id>/', news_detail, name='news_detail'),
    path('search_results/', search_results, name='search_results'),
    path('category/<int:category_id>/', category_page, name='category'),
    path('faculty_detail/<int:faculty_id>/', faculty_detail, name='faculty_detail'),
]