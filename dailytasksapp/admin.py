from django.contrib import admin
from .models import DailyTask

class DailyTaskAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)
    

admin.site.register(DailyTask, DailyTaskAdmin)
