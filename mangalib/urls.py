from django.urls import path
from . import views

app_name = "mangalib"

urlpatterns = [
    path('', views.index, name='index'), # manga/
    path('<int:book_id>/', views.show, name='show'), # manga/<id>
    path('Ajouter-livre/', views.add, name = 'add'),
    path('modifier-livre/<int:book_id>/', views.edit, name = 'edit'),
    path('Supprimer-livre/<int:book_id>/', views.remove, name='delete')
]