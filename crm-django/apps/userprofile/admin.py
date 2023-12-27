from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    extra = 1
    max_num = 1
    min_num = 1
    can_delete = False
    classes = ('collapse',)
    show_change_link = True


class ProfileUserAdmin(UserAdmin):
    inlines = [ProfileInline]

class MyUserAdmin(admin.ModelAdmin):
    inlines = [ProfileInline]
    list_display = 'username', 'email', 'is_staff', 'is_superuser', 'last_login',
    list_filter = 'is_staff',
    search_fields = 'username', 'email'


# unregister old user admin
admin.site.unregister(User)
# register new user admin
admin.site.register(User, MyUserAdmin)

