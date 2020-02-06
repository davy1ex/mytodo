from django.contrib import admin
from django.urls import path

import tasks.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tasks.views.all),
    path('tasks/all/', tasks.views.all),
]
