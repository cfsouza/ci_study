from django.contrib import admin

from reversion.admin import VersionAdmin

from .models import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(VersionAdmin):

    pass
