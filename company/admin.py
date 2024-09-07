from django.contrib import admin
from .models import employee,Testimonial
# Register your models here.
class adminModel(admin.ModelAdmin):
    list_display = ('name','employee_id','Working','address')
    search_fields = ('name','Working')
    list_editable = ['Working','address']
    list_filter = ('address',)





admin.site.register(employee,adminModel)
admin.site.register(Testimonial)

