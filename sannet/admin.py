from django.contrib import admin
import models
# Register your models here.

class SystemAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('name','comment')

admin.site.register(models.System,SystemAdmin)

class DeviceTypeAdmin(admin.ModelAdmin):

	def showBelongSystem(self,belongSystem):
		return belongSystem.name
	
	list_per_page = 10
	list_display = ('name','belongSystem')


admin.site.register(models.DeviceType,DeviceTypeAdmin)

class DeviceAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('name','deviceType','deviceModel','comp','price','compTel')

admin.site.register(models.Device,DeviceAdmin)

class ProjectAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('pname','position','comp','startTime','finishedTime')

admin.site.register(models.Project,ProjectAdmin)

class ProjectDeviceAdmin(admin.ModelAdmin):
	list_per_page = 10
	list_display = ('device','deviceNum','project')

admin.site.register(models.ProjectDevice,ProjectDeviceAdmin)

