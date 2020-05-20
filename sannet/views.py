#coding:utf-8
from django.shortcuts import render_to_response
from django.contrib import auth
from django.http.response import HttpResponseRedirect
import models

# Create your views here.

def index(req):	
	username = req.COOKIES.get("username")	
	if username is None:
		return HttpResponseRedirect('/login/')
	
	projects = models.Project.objects.all()
	
	return render_to_response('index.htm',{'username':username,'projects':projects})

def login(req):
	if req.method =='POST':
		username = req.POST.get('username')
		password = req.POST.get('password')
		user = auth.authenticate(username=username,password=password)

		if user is not None:
			response = HttpResponseRedirect('/index/')
			u = auth.admin.User.get_short_name(user)
			print u
			response.set_cookie("username", u, 3600)
			return response
		else:
			
			return HttpResponseRedirect('/login/')
	return render_to_response('login.htm',{})

def logout(req):
	response = HttpResponseRedirect('/login/')
	response.delete_cookie('username')
	return response

def proj_detail(req,proj_id):
	username = req.COOKIES.get("username")	
	if username is None:
		return HttpResponseRedirect('/login/')
	
	projects = models.Project.objects.filter(id=proj_id)
	#debug port 
	#for project in projects:
	#	print project.pname,project.finishedTime
	
	return render_to_response('proj_detail.htm',{'username':username,'projects':projects})

def project_device(req,project_name):
	username = req.COOKIES.get("username")	
	if username is None:
		return HttpResponseRedirect('/login/')

	project = models.Project.objects.get(id=project_name)
	#debug port 
# 	print project
	projectdevices = models.ProjectDevice.objects.filter(project=project)
	#debug port    
# 	for projectdevice in projectdevices:
# 		print projectdevice.device
		
	return render_to_response('project_device.htm',{'username':username,'projectdevices':projectdevices})

def device_list(req):
	username = req.COOKIES.get("username")	
	if username is None:
		return HttpResponseRedirect('/login/')
	
	devices = models.Device.objects.all()
	
	
	return render_to_response('device_list.htm',{'username':username,'devices':devices})

def device_detail(req,device_id):
	username = req.COOKIES.get("username")	
	if username is None:
		return HttpResponseRedirect('/login/')
	
	devices = models.Device.objects.filter(id=device_id)
	for device in devices:
		print device.name
	
	return render_to_response('device_detail.htm',{'username':username,'devices':devices})






























