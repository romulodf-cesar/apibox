
from django.contrib import admin
from django.urls import path
from apibox_app.views import box

urlpatterns = [
    path('admin/', admin.site.urls),
    path('box/', box, name='box'),
]
