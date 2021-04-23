from django.urls import path
from . import views


app_name = 'webapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('info',views.info,name='info'),
    path('create/<int:lat_int>/<int:lat_flo>/<int:lng_int>/<int:lng_flo>',views.create,name='create'),
    path('update/<int:num>',views.update,name='update'),
    path('delete/<int:num>',views.delete,name='delete'),
]