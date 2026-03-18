from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Role & Location', {'fields': ('role', 'agency', 'sub_city', 'woreda')}),
    )
    list_display = ('username', 'email', 'role', 'agency', 'sub_city', 'woreda', 'is_staff')
