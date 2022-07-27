from django.contrib import admin

from Dangky.views import dangky
from Dangky.models import NguoiDung

# Register your models here.

class NguoiDungAdmin(admin.ModelAdmin):
    list_display = ('ten_dang_nhap', 'email', 'mat_khau')
    list_display_links=('ten_dang_nhap', 'email', 'mat_khau')
    list_filter=('ten_dang_nhap', 'email', 'mat_khau')
    search_fields=('ten_dang_nhap', 'email', 'mat_khau')
    list_per_page=20

admin.site.register(NguoiDung, NguoiDungAdmin)