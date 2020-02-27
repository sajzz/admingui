from django.contrib import admin

# Register your models here.
from .models import admingui

admin.site.site_header ="VNIT ADMINSTRATION"
admin.site.site_title = "VNIT ADM."
admin.site_index_title ="Welcome to VNIT "

admin.site.register(admingui)
