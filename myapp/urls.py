# myapp/urls.py
from django.urls import path
from .views import home, asset_management, daily_zoo_activity, management_reporting, view_table, insert_table, update_table

urlpatterns = [
    path('', home, name='home'),
    path('asset_management/', asset_management, name='asset_management'),
    path('daily_zoo_activity/', daily_zoo_activity, name='daily_zoo_activity'),
    path('management_reporting/', management_reporting, name='management_reporting'),
    # Add more URLs as needed
    path('view_table/<str:table_name>/', view_table, name='view_table'),
    path('insert_table/<str:table_name>/', insert_table, name='insert_table'),
    path('update_table/<str:table_name>/', update_table, name='update_table'),

]
