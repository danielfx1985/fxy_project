# Generated by Django 4.1.2 on 2023-02-10 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=500, verbose_name='姓名')),
                ('minzu', models.CharField(default='傣', max_length=50)),
                ('birth_date', models.DateTimeField()),
                ('age', models.IntegerField()),
                ('sfid', models.CharField(blank=True, default='', max_length=18, null=True, verbose_name='身份证号码')),
                ('tel', models.CharField(default='', max_length=150)),
                ('hukou', models.CharField(choices=[('农村户口', '农村户口'), ('城镇户口', '城镇户口')], default='', max_length=150)),
                ('adress', models.CharField(default='', max_length=150)),
                ('dhamma_name', models.CharField(default='', max_length=500)),
                ('title2', models.CharField(choices=[('沙马内拉', '沙马内拉'), ('比库', '比库')], default='沙马内拉', max_length=50)),
                ('teacher_id', models.IntegerField(default=1)),
                ('monk_date', models.DateTimeField()),
                ('monk_temple', models.CharField(default='', max_length=500)),
                ('sila_teacher', models.CharField(default='', max_length=500)),
                ('grade', models.IntegerField(default=1)),
                ('base_id', models.IntegerField(default=1)),
                ('religion_id', models.IntegerField(default=1)),
                ('study_level', models.CharField(default='中专', max_length=500)),
                ('student_type', models.CharField(choices=[('全日制', '全日制'), ('非全日制', '非全日制')], default='全日制', max_length=500)),
                ('school_lenth', models.IntegerField(default=3)),
                ('enrol_date', models.DateTimeField()),
                ('middle_exam', models.BooleanField(default=True)),
                ('graduate_school', models.CharField(max_length=50)),
                ('relationship1', models.CharField(default='', max_length=50)),
                ('fml_name1', models.CharField(default='', max_length=50)),
                ('minzhu1', models.CharField(default='', max_length=50)),
                ('job_info1', models.CharField(default='', max_length=50)),
                ('fml_tel1', models.CharField(default='', max_length=50)),
                ('fml_id_f1', models.ImageField(blank=True, null=True, upload_to='')),
                ('fml_id_b1', models.ImageField(blank=True, null=True, upload_to='')),
                ('relationship2', models.CharField(blank=True, default='', max_length=50)),
                ('fml_name2', models.CharField(blank=True, default='', max_length=50)),
                ('minzhu2', models.CharField(blank=True, default='', max_length=50)),
                ('job_info2', models.CharField(blank=True, default='', max_length=50)),
                ('fml_tel2', models.CharField(blank=True, default='', max_length=50)),
                ('fml_id_f2', models.ImageField(blank=True, null=True, upload_to='')),
                ('fml_id_b2', models.ImageField(blank=True, null=True, upload_to='')),
                ('relationship3', models.CharField(blank=True, default='', max_length=50)),
                ('fml_name3', models.CharField(blank=True, default='', max_length=50)),
                ('minzhu3', models.CharField(blank=True, default='', max_length=50)),
                ('job_info3', models.CharField(blank=True, default='', max_length=50)),
                ('fml_tel3', models.CharField(blank=True, default='', max_length=50)),
                ('fml_id_f3', models.ImageField(blank=True, null=True, upload_to='')),
                ('fml_id_b3', models.ImageField(blank=True, null=True, upload_to='')),
                ('relationship4', models.CharField(blank=True, default='', max_length=50)),
                ('fml_name4', models.CharField(blank=True, default='', max_length=50)),
                ('minzhu4', models.CharField(blank=True, default='', max_length=50)),
                ('job_info4', models.CharField(blank=True, default='', max_length=50)),
                ('fml_tel4', models.CharField(blank=True, default='', max_length=50)),
                ('fml_id_f4', models.ImageField(blank=True, null=True, upload_to='')),
                ('fml_id_n4', models.ImageField(blank=True, null=True, upload_to='')),
                ('relationship5', models.CharField(blank=True, default='', max_length=50)),
                ('fml_name5', models.CharField(blank=True, default='', max_length=50)),
                ('minzhu5', models.CharField(blank=True, default='', max_length=50)),
                ('job_info5', models.CharField(blank=True, default='', max_length=50)),
                ('fml_tel5', models.CharField(blank=True, default='', max_length=50)),
                ('fml_id_f5', models.ImageField(blank=True, null=True, upload_to='')),
                ('fml_id_b5', models.ImageField(blank=True, null=True, upload_to='')),
                ('jiasha_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('clothes_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('ID_f_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('ID_b_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('FamilyAc_m_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('FamilyAc_p_photo', models.ImageField(blank=True, null=True, upload_to='')),
                ('security', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
