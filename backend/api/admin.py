from django.contrib import admin

# Register your models here.
from api.models import tourmodel

class Uploadadmin(admin.ModelAdmin):
    list_display = ['name','photo']

    class Meta:
        model = tourmodel.Pictures


admin.site.register(tourmodel.Pictures,Uploadadmin)
