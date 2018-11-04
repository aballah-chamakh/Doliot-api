from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminCreationForm, UserAdminChangeForm
from .models import User,Profile

class UserAdmin(BaseUserAdmin):
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    list_display = ('email', 'username','admin')
    list_filter = ('admin',)
    fieldsets = (
        (None, {'fields': ('email','username', 'password')}),
        ('Personal info', {'fields': ()}),
        ('Permissions', {'fields': ('active','staff','admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username','password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('admin',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.register(Profile)
