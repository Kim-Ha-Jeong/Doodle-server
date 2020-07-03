from django.contrib import admin
from .models import *


# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = '__all__'


class ProduceAdmin(admin.ModelAdmin):
    list_display = '__all__'


admin.site.register(Review, ReviewAdmin)
admin.site.register(Produce, ProduceAdmin)
