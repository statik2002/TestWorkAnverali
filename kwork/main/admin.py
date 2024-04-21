from django.contrib import admin

from main.models import Customer


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'is_active', 'is_customer')
    list_editable = ('is_active',)
    list_display_links = ('id', 'username')
    list_filter = ('is_active', 'is_customer')
    search_fields = ('id', 'username', 'first_name', 'last_name')
