from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class UserAdminView(UserAdmin):
    list_display = ["email", "username"]
    add_fieldsets = (
        ("Personal info", {"fields": ('first_name',
         'last_name', 'username', 'email', 'phone_number',)}),
        ("Permissions", {
         "fields": ('is_staff', 'is_superuser', "is_active",)}),
        ("Password", {"fields": ('password1', 'password2',)}),
    )



