from django.contrib import admin

from reversion.admin import VersionAdmin

from .models import Post

# Register your models here.
# admin.site.unregister(Post)

@admin.register(Post)
class PostAdmin(VersionAdmin):

    pass
# admin.site.register(Post)
