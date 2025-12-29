from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Role, JournalAction

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Informations SEAD', {'fields': ('role_systeme', 'role_mcd', 'telephone', 'organisme', 'statut')}),
    )

admin.site.register(Role)
admin.site.register(JournalAction)