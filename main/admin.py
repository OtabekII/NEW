from django.contrib import admin
from . import models

admin.site.register(models.Blog)
admin.site.register(models.BlogImg)
admin.site.register(models.BlogVideo)
admin.site.register(models.Comment)
admin.site.register(models.UserProfile)
admin.site.register(models.Post)
# admin.site.register(models.Comment)
admin.site.register(models.Like)
admin.site.register(models.Tarmoq)

