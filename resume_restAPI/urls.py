"""
URL configuration for resume_restAPI project.

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
from django.urls import path
from .views import index, upload_resume, process_resume, get_resume_data

from django.urls import path
from .views import index, upload_resume, process_resume, get_resume_data

urlpatterns = [
    path('', index, name='index'),
    path('upload', upload_resume, name='upload_resume'), # add this line
    path('process', process_resume, name='process'),
    path('resume/<int:resume_id>/', get_resume_data, name='resume_data'),
]