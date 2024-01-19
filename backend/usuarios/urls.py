from django.urls import path

from . import views as v

app_name = 'usuarios'

urlpatterns = [
   path('membro_list/<int:pk>/', v.membro_list, name='membro_list'),
   path('endereco_titular/<int:pk>/', v.endereco_titular, name='endereco_titular'),
   path('', v.titular_list, name='titular_list'),
   path('<int:pk>/', v.titular_detail, name='titular_detail'),

]
