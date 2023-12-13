"""
URL configuration for ToDo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import get_Task,save_Task,get_By_Id_Task,update_Task,delete_Task,home

urlpatterns = [
        path('', home, name='home'),
        path('api/get-tasks/', get_Task, name='get_Task'),  
    path('api/save-tasks/', save_Task, name='save_Task'),  
 path('api/getById-tasks/<int:task_id>/', get_By_Id_Task, name='get_By_Id_Task'),
    path('api/<int:task_id>/update-tasks/', update_Task),
    path('api/<int:task_id>/delete-tasks/', delete_Task),
    path('admin/', admin.site.urls),
]
