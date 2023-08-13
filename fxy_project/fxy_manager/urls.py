"""fxy_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from .views import one_info, index, export_xls, add_newstu_success,update_student_success,delete_student_success,add_newTeacher_success, student_info_ListView, teacher_info_ListView, \
    searchStuInfo, export_xlsx, student_info_TableList, student_info_create, student_info_Update, student_info_Delete, \
    teacher_info_create, teacher_info_Update, teacher_info_Delete, stuInfoList_API, export_students_xls,update_teacher_success,delete_teacher_success,one_info_teacher

stuInfo_list = stuInfoList_API.as_view(
    {'get': 'list',
     'post': 'create'}
)
router = routers.DefaultRouter()
router.register(r'stu_info', viewset=stuInfoList_API)
urlpatterns = [
    path('export_xls', export_xls),
    #path('', index, name='index'),
    path('student_info/', student_info_ListView.as_view(), name='student_info'),

    #path('', student_info_ListView.as_view(), name='student_info'),
    path('teachers/teacher_info/', teacher_info_ListView.as_view(), name='teacher_info'),
    path('student_info_table/', student_info_TableList, name='student_info_table'),
    #  path('add/',addNewStu,name='add'),
    path('add/', student_info_create.as_view(), name='add'),
    path('add_newstu_success/', add_newstu_success, name='add_newstu_success'),
    path('update_student_success/', update_student_success, name='update_student_success'),
    path('delete_student_success/', delete_student_success, name='delete_student_success'),
    path('teachers/add_teacher/', teacher_info_create.as_view(), name='add_teacher'),
    path('<int:pk>/print', one_info.as_view(), name='print'),
    path('teachers/<int:pk>/print', one_info_teacher.as_view(), name='print'),
    path('teachers/<pk>/update', teacher_info_Update.as_view(), name='updateTR'),
    path('teachers/<pk>/delete', teacher_info_Delete.as_view(), name='deleteTR'),
    path('<pk>/update', student_info_Update.as_view(), name='update'),
    path('<pk>/delete', student_info_Delete.as_view(), name='delete'),

    path('teachers/add_newTeacher_success', add_newTeacher_success, name='add_newTeacher_success'),
    path('teachers/update_teacher_success', update_teacher_success, name='update_teacher_success'),
    path('teachers/delete_teacher_success', delete_teacher_success, name='delete_teacher_success'),

    path('searchStu', searchStuInfo, name='searchStuInfo'),
    # path('<pk>/export_xlsx',export_xlsx,name='export_xlsx'),
    path('api/', include(router.urls)),

    path('<pk>/export_xls', export_students_xls, name='export_xls'),
]
