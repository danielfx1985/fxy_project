from django import forms
from .models import student_info,teacher_info


class addInfoForm(forms.ModelForm):
    class Meta:
        model=student_info
        fields=("__all__")
        '''labels={
            "name":"姓#--名",
            "minzu":"民族",
            "birth_date": "出生日期",
            "age": "年龄",
            "tel": "电话",
            "adress": "地址",
        }'''

class addInfoForm_teacher(forms.ModelForm):
    class Meta:
        model=teacher_info
        fields=("__all__")

