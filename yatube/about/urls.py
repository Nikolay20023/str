from django.urls import path
from posts.views import kurs_edit, index_2

app_name = 'about'

urlpatterns = [
    path('author/', index_2, name='author'),
    path('tech/', kurs_edit, name='tech'),
]
