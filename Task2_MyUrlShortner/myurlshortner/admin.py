from django.contrib import admin
from myurlshortner.models import UrlKey


class UrlKeyAdmin(admin.ModelAdmin):
    list_display = ('id', 'key_name', 'is_assigned', 'assigned_timestamp', 'assigned_url')
    search_fields = (['key_name'])


admin.site.register(UrlKey, UrlKeyAdmin)
