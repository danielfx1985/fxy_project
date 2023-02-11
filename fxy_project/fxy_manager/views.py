from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render,redirect
import xlwt
from django_tables2 import SingleTableView
import django_tables2 as tables
from django_tables2.export.views import ExportMixin
from django_tables2.export.export import TableExport
from .forms import  addInfoForm
# Create your views here.
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView,ListView,DetailView
from .tables import StuInfoTable
from .models import student_info
import logging
from rest_framework import serializers,viewsets,generics
from rest_framework.views import APIView
from .serializers import student_info_serializer
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
import datetime
import django_excel as excel
from django.db.models import F
import pyexcel

def export_xls(request):
    if request.method=="GET":
        print("requets=GET: " ,request.GET.get('name'))

   # print(" self  :  ",self.request)
    data_excel=student_info.objects.filter(name='王宗仁')#.annotate(new_name=F('name')).values('姓名')
    col_names=["name","minzu","birth_date","age","tel","adress","dhamma_name","title2","teacher_id"]
    return excel.make_response_from_query_sets(data_excel,col_names,'xlsx',status=200,file_name='tests')
   ## return excel.make_response_from_a_table(books,'xls',status=200,file_name='tests')

logger = logging.getLogger(__name__)
def index(request):
    return  render(request,'manager/index.html')


class student_info_ListView(generic.ListView):
    model=student_info
    context_object_name='student_info'
    template_name='manager/infoList.html'

#class stuInfo_viewSet(viewsets.ModelViewSet):
 #   queryset = student_info.objects.all()
  #  serializer_class = student_info_serializer

class stuInfoList_API(viewsets.ModelViewSet):
    queryset = student_info.objects.all()
    serializer_class = student_info_serializer

class studentifoDetail(APIView):
    """
    Retrieve, update or delete an article instance.
    """
    def get_object(self, pk):
        try:
            return student_info.objects.get(pk=pk)
        except student_info.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        studentifo = self.get_object(pk)
        serializer = student_info_serializer(studentifo)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        studentifo = self.get_object(pk)
        serializer = student_info_serializer(instance=studentifo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        studentifo = self.get_object(pk)
        studentifo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class one_info(DetailView):
    model = student_info
    template_name = "manager/stu_info_table.html"
    context_object_name = "stu_info"


class student_info_Update(generic.UpdateView):
    model=student_info
    form_class = addInfoForm
 #   context_object_name='student_info_update'
   # fields = "__all__"
    template_name='manager/infoUpate.html'
    success_url = "/manager/add_newstu_success"
class student_info_Delete(generic.DeleteView):
    model=student_info
    template_name = 'manager/deleting.html'
    print("deleting")
 #   context_object_name='student_info_update'
    fields = "__all__"
   # template_name='manager/infoUpate.html'
    success_message = "Deleted Successfully"
    success_url = "/manager/add_newstu_success"

class student_info_create(generic.CreateView):

    model=student_info
    form_class = addInfoForm
   # fields = "__all__"
    #print("sss")


 #   context_object_name='student_info_create'
    template_name='manager/infoCreate.html'
    success_url = "/manager/add_newstu_success"
    def form_invalid(self, form):
        logger.info('form_valid called')
        form.instance.user = self.request.user
        return super(student_info_create, self).form_valid(form)
    def form_valid(self, form):
        logger.info('form_valid called')
        form.instance.user = self.request.user
        return super(student_info_create, self).form_valid(form)
def student_info_TableList(request):

    table=StuInfoTable(student_info.objects.all())
   # template_name='manager/infoTableList.html'
    return render(request,"manager/infoTableList.html",{"table":table})


   # def get_queryset(self):
      # return student_baseInfo.
def add(request):
    pass
'''def addNewStu(request):
    if request.method=="POST":
        form=addBaseInfoForm(request.POST)
        form2=addFamilyInfoForm(request.POST)
        if all([form.is_valid(),form2.is_valid()]):
            post=form.save()
            post=form2.save()
            form2.is_valid()
            return redirect('add_newstu_success')
            #return redirect('/manager/add_newstu_success')
    else:
        form=addBaseInfoForm()
        form2 = addFamilyInfoForm()
  #  return render(request,'manager/add_edit.html',{'form':form,'form2':form2})
    return render(request, 'manager/infoAdd.html', {'form': form, 'form2': form2})
def add_newstu_success(request):
    return  render(request,'manager/add_newstu_success.html')
'''
def addNewStu(request):
    if request.method=="POST":
        form=addInfoForm(request.POST)

        form2=addFamilyInfoForm(request.POST)
        if  all([form.is_valid(),form2.is_valid()]):

            post=form.save()
            post2=form2.save()
           # form2.is_valid()
            return redirect('add_newstu_success')
        else:
            for field in form2:
                print("Field Error:", field.name,  field.errors)
            #return redirect('/manager/add_newstu_success')
    else:
        form=addInfoForm()
        form2 = addFamilyInfoForm()
    return render(request,'manager/infoCreate.html',{'form':form,'form2':form2})


def add_newstu_success(request):
    return  render(request,'manager/add_newstu_success.html')

def searchStuInfo(request):
    q=request.GET.get('q')
    error_msg=''
    print('q',q)
    if not q:
        error_msg = '请输入关键词'
        return HttpResponse("请输入关键词!")
    stuInfo=student_info.objects.filter(name__icontains=q)

    return render(request, 'manager/infoList.html', {'student_info': stuInfo})

'''
class TableView(ExportMixin, tables.SingleTableView):
    table_class = MyTable
    model = student_info
    template_name = "django_tables2/bootstrap.html"
    '''
def export_xlsx(request):
    export_format = request.GET.get('_export', None)

    if TableExport.is_valid_format(export_format):
        table = student_info
        exporter = TableExport(export_format, table)
        return exporter.response('table.{}'.format(export_format))



def export_students_xls(request,pk):
    print(pk)
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="users.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('student')
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['姓名', '民族', '出生日期','年龄','身份证号','联系电话','家庭住址','法名','教职身份','教职人员编号','出家年月','出家寺院',
               '戒师','年级','学号（国民教育）','学号（宗教学籍）','学历层次','学生类别','学制','入学日期','是否参加中考','毕业学校']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    rows = student_info.objects.filter(id=pk).all().values_list('name', 'minzu','birth_date', 'age','sfid','tel','adress','dhamma_name',
                                                                'title2','teacher_id','monk_date','monk_date','sila_teacher','grade','base_id',
                                                                'religion_id','study_level','student_type','school_lenth','enrol_date','middle_exam','graduate_school')
    print(rows)
    rows = [[x.strftime("%Y-%m-%d") if isinstance(x, datetime.datetime) else x for x in row] for row in rows]
     #??????
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
    wb.save(response)
    return response