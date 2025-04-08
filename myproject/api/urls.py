from django.urls import path, include
from .views import user_list
from django.contrib import admin

urlpatterns = [
    path('users/', user_list, name='user-list'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls'))
]
