import django_tables2 as tables
from django.utils.html import format_html
from django.urls import reverse
from .models import student_info

class StuInfoTable(tables.Table):
    class Meta:
        model=student_info
        #template_name = 'stuManage/infoList.html'
        #fields=("name",)
        '''labels={
            "name":"姓名",
            "minzu":"民族",
            "birth_date": "出生日期",
            "age": "年龄",
            "tel": "电话",
            "adress": "地址",
        }'''
        attrs = {"class": "table table-striped table-sm text-nowrap"}

