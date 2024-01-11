from django.urls import path
from .views import *

urlpatterns = [
    path('', BooksView.as_view({'get':'list', 'post': 'create'})),
    path('all/', allBooks),
    path('book/<int:pk>', getBook),
    path('create/', create),
    path('update/<int:pk>', update),
    path('delete/<int:pk>', delete),
]