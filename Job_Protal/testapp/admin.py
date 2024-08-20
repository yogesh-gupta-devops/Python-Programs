from django.contrib import admin
from testapp.models import PuneJobs, BngJobs, HydJobs

# Register your models here.
class HydJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligiblity', 'address', 'email', 'phonenumber']
admin.site.register(HydJobs, HydJobsAdmin)

class BngJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligiblity', 'address', 'email', 'phonenumber']
admin.site.register(BngJobs, BngJobsAdmin)

class PuneJobsAdmin(admin.ModelAdmin):
    list_display = ['date', 'company', 'title', 'eligiblity', 'address', 'email', 'phonenumber']
admin.site.register(PuneJobs, PuneJobsAdmin)