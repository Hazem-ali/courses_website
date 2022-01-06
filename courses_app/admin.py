from django.contrib import admin

from courses_app import models
# Register your models here.

# makes userprofile accessible on admin interface
admin.site.register(models.UserProfile)
