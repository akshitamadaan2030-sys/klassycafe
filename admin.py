from django.contrib import admin
from TableReservation.models import table_reserveration
class Table_Admin(admin.ModelAdmin):
    list_display=("tagline","des","icon_1","icon_2","phone_1","phone_2","email_1","email_2")
admin.site.register(table_reserveration,Table_Admin)
# Register your models here.
