from django.contrib import admin

from courses_app import models
# Register your models here.

# makes userprofile accessible on admin interface
admin.site.register(models.UserProfile)
admin.site.register(models.Course)
admin.site.register(models.Category)
