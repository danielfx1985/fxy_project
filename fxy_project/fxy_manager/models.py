from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField, DateField
# Create your models here.
class student_info(models.Model):
    #基本信息
    objects = models.Manager()
    name = models.CharField(verbose_name='姓名',max_length=500,default="")  # 姓名
    shengao =models.FloatField(verbose_name="身高",max_length=200,default=165)
    minzu = models.CharField(max_length=50,default="傣");  # 民族
    birth_date = models.DateTimeField()  # 出生日期
    age = models.IntegerField()  # 年龄
    sfid=models.CharField("身份证号码",default="",max_length=18,
   # unique = True, validators = [IDValidator],
                          null=True,blank=True)
    tel = models.CharField(max_length=150,default="")  # 联系电话
    hk = (('农村户口', '农村户口'), ('城镇户口', '城镇户口'))
    hukou = models.CharField(max_length=150,choices=hk ,default="")
    adress = models.CharField(max_length=150,default="")  # 地址
    # 宗教信息
    dhamma_name = models.CharField(max_length=500,default="")
    t2 = (('沙马内拉', '沙马内拉'), ('比库', '比库'))
    title2 = models.CharField(max_length=50, choices=t2,default="沙马内拉")  # 教职身份
    teacher_id = models.IntegerField(default=1)  # 教职人员编号（无/输入）
    monk_date = models.DateTimeField()  # 出家年月（2000-01-01）
    monk_temple = models.CharField(max_length=500,default="")  # 出家寺院
    sila_teacher = models.CharField(max_length=500,default="")  # 戒师
    # 学校信息
    grade = models.IntegerField(default=1)  # 年级
    base_id = models.IntegerField(default=1)  # 学号（国民教育）
    religion_id = models.IntegerField(default=1)  # 学号（宗教教育）
    sl = (('中专', '中专'), ('静修', '静修'))
    study_level = models.CharField(max_length=500,default="中专")  # 学历层次（中专/静修）
    st = (('全日制', '全日制'), ('非全日制', '非全日制'))
    student_type = models.CharField(max_length=500,choices=st,default="全日制")  # 全日制、非全日制
    school_lenth = models.IntegerField(default=3)  # 学制
    enrol_date = models.DateTimeField()  # 入学日期
    middle_exam = models.BooleanField(default=True)  # 是否参加中考
    graduate_school = models.CharField(max_length=50)  # 毕业学校
    # 家庭信息

    relationship1 = models.CharField(max_length=50,default="")  # 家属关系1
    fml_name1=models.CharField(max_length=50,default="")#家属姓名1
    minzhu1=models.CharField(max_length=50,default="")#民族1
    #family_id=models.IntegerField()#家长ID1
    job_info1=models.CharField(max_length=50,default="")#工作单位及职务1
    fml_tel1=models.CharField(max_length=50,default="")#联系方式（检测11位）1
    fml_id_f1 = models.ImageField(null=True, blank=True)
    fml_id_b1 = models.ImageField(null=True, blank=True)

    relationship2 = models.CharField(max_length=50,default="",blank=True)  # 家属关系1
    fml_name2 = models.CharField(max_length=50,default="",blank=True)  # 家属姓名1
    minzhu2 = models.CharField(max_length=50,default="",blank=True)  # 民族1
    # family_id=models.IntegerField()#家长ID1
    job_info2 = models.CharField(max_length=50,default="",blank=True)  # 工作单位及职务1
    fml_tel2 = models.CharField(max_length=50,default="",blank=True) # 联系方式（检测11位）1
    fml_id_f2 = models.ImageField(null=True, blank=True)
    fml_id_b2 = models.ImageField(null=True, blank=True)

    relationship3 = models.CharField(max_length=50,default="",blank=True)  # 家属关系1
    fml_name3 = models.CharField(max_length=50,default="",blank=True)  # 家属姓名1
    minzhu3 = models.CharField(max_length=50,default="",blank=True)  # 民族1
    # family_id=models.IntegerField()#家长ID1
    job_info3 = models.CharField(max_length=50,default="",blank=True)  # 工作单位及职务1
    fml_tel3 = models.CharField(max_length=50,default="",blank=True) # 联系方式（检测11位）1
    fml_id_f3 = models.ImageField(null=True, blank=True)
    fml_id_b3 = models.ImageField(null=True, blank=True)

    relationship4 = models.CharField(max_length=50,default="",blank=True)  # 家属关系1
    fml_name4 = models.CharField(max_length=50,default="",blank=True)  # 家属姓名1
    minzhu4 = models.CharField(max_length=50,default="",blank=True)  # 民族1
    # family_id=models.IntegerField()#家长ID1
    job_info4= models.CharField(max_length=50,default="",blank=True)  # 工作单位及职务1
    fml_tel4 = models.CharField(max_length=50,default="",blank=True)  # 联系方式（检测11位）1
    fml_id_f4 = models.ImageField(null=True, blank=True)
    fml_id_n4 = models.ImageField(null=True, blank=True)

    relationship5 = models.CharField(max_length=50,default="",blank=True)  # 家属关系1
    fml_name5 = models.CharField(max_length=50,default="",blank=True)  # 家属姓名1
    minzhu5 = models.CharField(max_length=50,default="",blank=True)  # 民族1
    # family_id=models.IntegerField()#家长ID1
    job_info5 = models.CharField(max_length=50,default="",blank=True)  # 工作单位及职务1
    fml_tel5 = models.CharField(max_length=50,default="",blank=True) # 联系方式（检测11位）1
    fml_id_f5 = models.ImageField(null=True, blank=True)
    fml_id_b5 = models.ImageField(null=True, blank=True)
    #文件

    jiasha_photo=models.ImageField( null=True,blank=True,upload_to="./img/")
    clothes_photo = models.ImageField( null=True,blank=True,upload_to="./img/")
    ID_f_photo = models.ImageField( null=True,blank=True,upload_to="./img/")
    ID_b_photo = models.ImageField( null=True,blank=True,upload_to="./img/")
    FamilyAc_m_photo = models.ImageField( null=True,blank=True,upload_to="./img/")
    FamilyAc_p_photo = models.ImageField( null=True,blank=True,upload_to="./img/")
    security = models.ImageField( null=True,blank=True,upload_to="./img/")

class teacher_info(models.Model):
    objects = models.Manager()
    name = models.CharField(verbose_name='姓名', max_length=500, default="")  # 姓名
    pname = models.CharField(verbose_name='曾用名', max_length=500, default="无")  # 曾用名
    cxb = (('男', '男'), ('女', '女'))

    xb = models.CharField(max_length=10, choices=cxb, default="男")  # 性别
    age = models.IntegerField( default=20)  # 年龄
    birth_date = models.DateTimeField(default=None)  # 出生日期
    minzu = models.CharField(max_length=50, default="傣");  # 民族
    jiguan = models.CharField(max_length=50, default="");  # 籍贯

    zm = (('党员', '党员'), ('团员', '团员'), ('群众', '群众'))
    zzmm = models.CharField(max_length=10, choices=zm, default="群众")  # 政治面貌
    rdsj = models.DateTimeField(default=None,blank=True)   # 入党时间
    whcd = models.CharField(max_length=50, default="");  # 文化程度
    hy = (('未婚', '未婚'), ('已婚', '已婚'), ('离异', '离异'), ('丧偶', '丧偶'))
    hyzk = models.CharField(max_length=50, choices=hy,default="");  # 婚姻状况

    sfid = models.CharField("身份证号码", default="", max_length=18,
                            # unique = True, validators = [IDValidator],
                            null=True, blank=True)
    tel = models.CharField(max_length=150, default="")  # 联系电话
    adress=models.CharField(max_length=150, default="")

    title_context=(('三级','三级'),('二级','二级'),('一级','一级'),('高级','高级'))
    title = models.CharField(max_length=100,default="",choices=title_context)  # 职称
    position = models.CharField(max_length=100,default="")  # 职务/岗位
    level_context = (('高级讲师','高级讲师'), ('讲师','讲师'), ('助教','助教'))
    level = models.CharField(max_length=100,default="",choices=level_context)  # 职级
    work_desc = models.CharField(max_length=100,default="") # 分管工作

    cert_context = (('初级中学教师资格','初级中学教师资格'), ('高级中学教师资格','高级中学教师资格'), ('中等职业学校教师资格','中等职业学校教师资格'), ('中等职业学校实习指导教师资格','中等职业学校实习指导教师资格'), ('高等学校教师资格','高等学校教师资格'))
    cert = models.CharField(max_length=100,default="")  # 教师资格证
    chinese_level_context = (('一级','一级'), ('一级甲等','一级甲等'), ('一级乙等','一级乙等'), ('二级','二级'),('二级甲等','二级甲等'), ('二级乙等','二级乙等'), ('三级','三级'), ('三级甲等','三级甲等'),('三级乙等','三级乙等'))
    chinese_level = models.CharField(max_length=100,choices=chinese_level_context,default="")  # 普通话等级证书

    job1_st=models.DateTimeField(default=None,null=True,blank=True)#工作经历1起始时间
    job1_ed=models.DateTimeField(default=None,null=True,blank=True)#工作经历1结束时间
    job1_dw=models.CharField(max_length=100,default="",null=True,blank=True)#工作经历1单位
    job1_pt=models.CharField(max_length=100,default="",null=True,blank=True)#工作经历1职位
    job2_st=models.DateTimeField(default=None,null=True,blank=True)#工作经历1起始时间
    job2_ed=models.DateTimeField(default=None,null=True,blank=True)#工作经历1结束时间
    job2_dw=models.CharField(max_length=100,default="",null=True,blank=True)#工作经历1单位
    job2_pt=models.CharField(max_length=100,default="",null=True,blank=True)#工作经历1职位
    job3_st=models.DateTimeField(default=None,null=True,blank=True)#工作经历1起始时间
    job3_st=models.DateTimeField(default=None,null=True,blank=True)#工作经历1起始时间
    job3_ed=models.DateTimeField(default=None,null=True,blank=True)#工作经历1结束时间
    job3_dw=models.CharField(max_length=100,default="",null=True,blank=True)#工作经历1单位
    job3_pt=models.CharField(max_length=100,default="",null=True,blank=True)#工作经历1职位
    job4_st=models.DateTimeField(default=None,null=True,blank=True)#工作经历1起始时间
    job4_ed=models.DateTimeField(default=None,null=True,blank=True)#工作经历1结束时间
    job4_dw=models.CharField(max_length=100,default="",null=True,blank=True)#工作经历1单位
    job4_pt=models.CharField(max_length=100,default="",null=True,blank=True)#工作经历1职位
    job5_st=models.DateTimeField(default=None,null=True,blank=True)#工作经历1起始时间
    job5_ed=models.DateTimeField(default=None,null=True,blank=True)#工作经历1结束时间
    job5_dw=models.CharField(max_length=100,default="",null=True,blank=True)#工作经历1单位
    job5_pt=models.CharField(max_length=100,default="",null=True,blank=True)#工作经历1职位

    fm1_title = models.CharField(max_length=20,default="",null=True,blank=True) # 称谓
    fm1_name = models.CharField(max_length=100,default="",null=True,blank=True) # 姓名
    fm1_political_status = models.CharField(max_length=100,default="",null=True,blank=True) # 政治面貌,如中共党员
    fm1_work_unit = models.CharField(max_length=200,default="",null=True,blank=True) # 工作单位
    fm1_position = models.CharField(max_length=100,default="",null=True,blank=True) # 职务

    fm2_title = models.CharField(max_length=20,default="",null=True,blank=True) # 称谓
    fm2_name = models.CharField(max_length=100,default="",null=True,blank=True) # 姓名
    fm2_political_status = models.CharField(max_length=100,default="",null=True,blank=True) # 政治面貌,如中共党员
    fm2_work_unit = models.CharField(max_length=200,default="",null=True,blank=True) # 工作单位
    fm2_position = models.CharField(max_length=100,default="",null=True,blank=True) # 职务

    fm3_title = models.CharField(max_length=20,default="",null=True,blank=True) # 称谓
    fm3_name = models.CharField(max_length=100,default="",null=True,blank=True) # 姓名
    fm3_political_status = models.CharField(max_length=100,default="",null=True,blank=True) # 政治面貌,如中共党员
    fm3_work_unit = models.CharField(max_length=200,default="",null=True,blank=True) # 工作单位
    fm3_position = models.CharField(max_length=100,default="",null=True,blank=True) # 职务

    fm4_title = models.CharField(max_length=20,default="",null=True,blank=True) # 称谓
    fm4_name = models.CharField(max_length=100,default="",null=True,blank=True) # 姓名
    fm4_political_status = models.CharField(max_length=100,default="",null=True,blank=True) # 政治面貌,如中共党员
    fm4_work_unit = models.CharField(max_length=200,default="",null=True,blank=True) # 工作单位
    fm4_position = models.CharField(max_length=100,default="",null=True,blank=True) # 职务

class File(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    upload_time = models.DateTimeField(auto_now_add=True)
    file_size = models.PositiveIntegerField()

    def __str__(self):
        return self.name