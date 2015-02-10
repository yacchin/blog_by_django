from django.contrib import admin
from bootstrap_blog.models import *

# Register your models here.

admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(User)
admin.site.register(PostsTags)
