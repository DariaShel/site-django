from django.contrib import admin
from table.models import DashaTable
# Register your models here.
class DashaTable_Admin(admin.ModelAdmin):
	list_display = ('title','image','timestamp')

admin.site.register(DashaTable,DashaTable_Admin)

