from django.contrib import admin
from .models import Community

class CommunityAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content', 'create_date']

# Register your models here.
admin.site.register(Community, CommunityAdmin)