from django.urls import path
from . import views

app_name = 'articles' # permet de savoir que l'on fait référence à articles (application)
urlpatterns = [
    path('', views.index, name='articles'), # name sert avec les templates
]