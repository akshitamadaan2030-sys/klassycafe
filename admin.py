from django.contrib import admin
from weekorder.models import week
class week_admin(admin.ModelAdmin):
    list_display = ["week_img","week_name","week_des","week_price"]
admin.site.register(week,week_admin)
# Register your models here.
