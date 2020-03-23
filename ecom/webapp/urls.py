from django.contrib import admin
from django.urls import path
from webapp.views import index,get_categories,get_items,get_item_view

urlpatterns = [
    path('',index),
    path('categories',get_categories),
    path(r'categories/<int:id>',get_items),
    path(r'categories/items/<int:id>',get_item_view)
]