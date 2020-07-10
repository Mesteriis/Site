from django.contrib import admin
from .models import Profile, Notification, Task
from django.contrib.auth.models import User
from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)



class UserProfileInline(admin.StackedInline):
    model = Profile
#
#

class UserNotificationsInline(admin.StackedInline):
    model = Notification

class UserTasksInline(admin.StackedInline):
    model = Task

class UserProfileAdmin(UserAdmin):
    # inlines = [UserProfileInline]
    inlines = [ UserProfileInline, UserNotificationsInline, UserTasksInline ]


#
admin.site.register(User, UserProfileAdmin)

# admin.site.register(Profile)
# admin.site.register(User)
# admin.site.register(Notification)
# admin.site.register(Task)
