from django.contrib import admin
from .models import Post

# Register your models here.
class Register(admin.ModelAdmin):
    list_display_links = ('update',)
    list_display = ('title', 'timestamp', 'update')
    list_filter = ('timestamp',)
    list_editable = ('title', )


admin.site.register(Post, Register)

