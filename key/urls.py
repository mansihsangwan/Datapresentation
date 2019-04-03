from django.contrib import admin
from django.urls import path
from . import views
from .views import *
   
app_name = 'key'

urlpatterns = [
    path('', key_details, name='key_details'),
    path('keyword/', Add_keyword, name='keyword'),
    path('keyword_list/', Keyword_list, name='keyword_list'),
    path('keyword_list/keyword_que_list/<int:keyword_id>', keyword_que_list, name='keyword_que_list'),
    path('main/',main,name='main'),
    path('main/detail/<int:presentation_id>/',detailview, name='detailview'),
    path('main/deck/<int:presentation_id>/',deck, name='deck'),
    path('main/de/<int:keyword_id>/',de, name='de'),
    path('pdf/<int:presentation_id>/', views.GeneratePdf.as_view(), name='pdf'),
    path('keypdf/<int:keyword_id>/', views.KeyPdf.as_view(), name='keypdf'),
    path('ques/',views.manage, name='manage'),
    path('delete/<int:id>', views.que_delete, name='que_delete'),
    path('update/<int:id>', views.que_update, name='que_update'),
    path('delete/<int:detail_id>/', delete_slide, name='delete'),
    path('deletekeyword/<int:detail_id>/', delete_keyword_slide, name='deletekeyword'),
] 