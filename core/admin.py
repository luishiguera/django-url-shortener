from django.contrib import admin
from .models import Link

# Register your models here.
@admin.register(Link)
class Administrator(admin.ModelAdmin):
    list_display = ('url', 'code', 'counter')
    readonly_fields = ('code', 'date', 'counter')