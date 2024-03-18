from django.contrib import admin
from contact import models

@admin.register(models.Contact)

class ContactAdmin(admin.ModelAdmin):
    list_display = 'id','first_name','last_name','phone',
    ordering = 'id',
    list_filter = 'first_name','last_name','phone',
    search_fields = 'first_name','last_name',
    list_per_page = 10
    list_max_show_all = 100
# Register your models here.
    @admin.register(models.Category)
    class CategoryAdmin(admin.ModelAdmin):
    list_display = 'name',
    ordering = 'id',
   