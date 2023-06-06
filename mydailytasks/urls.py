"""
URL configuration for mydailytasks project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from dailytasksapp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication Urls
    path('signup/', views.signup_new_user, name='signupnewuser'),
    path('logout/', views.logout_user, name='logoutuser'),
    path('login/', views.login_user, name='loginuser'),

    # Tasks Urls
    path('home/', views.home, name='home'),
    path('create/', views.create_task, name='createtask'),
    path('completed/', views.completed_tasks, name='completedtasks'),

    path('current/', views.current_task, name='currentdailytasks'),
    path('viewtask/<int:task_pk>', views.view_task, name='viewtask'),
    path('viewtask/<int:task_pk>/complete', views.complete_task, name='completetask'),
    path('viewtask/<int:task_pk>/delete', views.delete_task, name='deletetask'),

]
