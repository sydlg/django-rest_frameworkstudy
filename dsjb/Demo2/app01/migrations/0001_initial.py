# Generated by Django 2.2 on 2020-04-17 14:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10, verbose_name='类目名')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
            options={
                'verbose_name': '商品类别',
                'verbose_name_plural': '商品类别',
            },
        ),
        migrations.CreateModel(
            name='Type2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10, verbose_name='类目名')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.Type1', verbose_name='父级类别')),
            ],
            options={
                'verbose_name': '商品类别2',
                'verbose_name_plural': '商品类别2',
            },
        ),
        migrations.CreateModel(
            name='Type3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10, verbose_name='类目名')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.Type2', verbose_name='父级类别')),
            ],
            options={
                'verbose_name': '商品类别3',
                'verbose_name_plural': '商品类别3',
            },
        ),
        migrations.CreateModel(
            name='Type4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=10, verbose_name='类目名')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app01.Type3', verbose_name='父级类别')),
            ],
            options={
                'verbose_name': '商品类别4',
                'verbose_name_plural': '商品类别4',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='类别名', max_length=30, verbose_name='类别名')),
                ('code', models.CharField(default='', help_text='类别code', max_length=30, verbose_name='类别code')),
                ('desc', models.CharField(default='', help_text='类别描述', max_length=30, verbose_name='类别描述')),
                ('category_Type', models.IntegerField(choices=[(1, '一级类目'), (2, '二级类目'), (3, '三级类目'), (4, '四级类目')], help_text='类别描述', verbose_name='类别描述')),
                ('is_tab', models.BooleanField(default=False, help_text='是否导航', verbose_name='是否导航')),
                ('parent_category', models.ForeignKey(blank=True, help_text='父类别', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub_cat', to='app01.Type', verbose_name='父类目录')),
            ],
            options={
                'verbose_name': '商品类别',
                'verbose_name_plural': '商品类别',
            },
        ),
    ]
