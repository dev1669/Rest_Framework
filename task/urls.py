from django.urls import path
from . import views

urlpatterns = [

            path('',views.home,name='home'),
            path('get_data/<int:pk>', views.api_access, name='get_data'),
]