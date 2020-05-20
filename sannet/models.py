# -*- coding:utf-8  -*-
from django.db import models

# Create your models here.
class System(models.Model):
	name = models.CharField(max_length=50,verbose_name='系统名称',unique=True)
	comment = models.TextField(verbose_name='系统说明')

	class Meta:
		verbose_name = '设备类别'
		verbose_name_plural = '设备类别'
	def __str__(self):
		return self.name

class DeviceType(models.Model):
	name = models.CharField(max_length=50,verbose_name='设备类型',unique=True)
	belongSystem = models.ForeignKey(System,verbose_name='类别')

	class Meta:
		verbose_name = '设备类型'
		verbose_name_plural = '设备类型'

	def __str__(self):
		return self.name


class Device(models.Model):
	name = models.CharField(max_length=50,verbose_name='名称',unique=True)
	deviceImage = models.ImageField(upload_to='uploads/devices/',verbose_name='设备图片',blank=True,null=True)
	deviceType = models.ForeignKey(DeviceType,verbose_name='设备类型')
	deviceModel = models.CharField(max_length=50,verbose_name='设备型号')
	comp = models.CharField(max_length=50,verbose_name='生产厂家')
	compTel = models.CharField(max_length=20,verbose_name='客服电话',blank=True,null=True)
	price =  models.PositiveSmallIntegerField(verbose_name='价格',blank=True,null=True)
	parameter = models.TextField(verbose_name='性能参数',blank=True,null=True)
	description = models.TextField(verbose_name='产品描述',blank=True,null=True)
	remark = models.TextField(verbose_name='备注',blank=True,null=True)
	
	class Meta:
		verbose_name = '设备'
		verbose_name_plural = '设备'

	def __str__(self):
		return self.name

class Project(models.Model):
	pname = models.CharField(max_length=100,verbose_name='项目名称',unique=True)
	position = models.CharField(max_length=100,verbose_name='施工地点')
	comp = models.CharField(max_length=100,verbose_name='施工单位')
	startTime = models.DateField(verbose_name='启动时间',null=True,blank=True)
	finishedTime = models.DateField(verbose_name='竣工时间',null=True,blank=True)
	config = models.FileField(upload_to='uploads/archives/',verbose_name='配置文件',null=True,blank=True)
	desc = models.TextField(verbose_name='描述信息',null=True,blank=True)	
	
	class Meta:
		verbose_name = "项目"
		verbose_name_plural = "项目"

	def __str__(self):
		return self.pname

class ProjectDevice(models.Model):
	device = models.ForeignKey(Device,verbose_name='设备名称')
	project = models.ForeignKey(Project,verbose_name='项目')
	deviceNum = models.PositiveSmallIntegerField(verbose_name='设备数量')

	class Meta:
		verbose_name = '项目设备'
		verbose_name_plural = '项目设备'

	def __str__(self):
		return self.device.name
