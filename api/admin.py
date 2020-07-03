from django.contrib import admin
from .models import Review, Produce


# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'star')


class ProduceAdmin(admin.ModelAdmin):
    list_display = ('order', 'o_phone_num', 'receiver', 'r_phone_num')


admin.site.register(Review, ReviewAdmin)
admin.site.register(Produce, ProduceAdmin)
