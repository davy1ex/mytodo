from django.contrib import admin
from django.urls import path

import tasks.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tasks.views.all),
    path('tasks/delete/<int:task_id>', tasks.views.delete, name="task_delete"),
    path('tasks/all/', tasks.views.all, name="task_all"),
    path('tasks/inbox/', tasks.views.inbox, name="task_inbox"),

]
