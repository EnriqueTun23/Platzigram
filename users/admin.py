#Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin
#Models
from .models import Profile
from django.contrib.auth.models import User
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'phone_number', 'website', 'created')
    list_display_links = ('pk', 'user')
    list_editable = ('phone_number', )
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'phone_number')
    list_filter = ('user__is_active', 'user__is_staff', 'created', 'modified' )
    fieldsets = (
        ('Profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields' : (('phone_number', 'website'), ('biography')),

        }),
        ('Metadata', {
            'fields' : (('created', 'modified'),),
        })
    )
    readonly_fields = ('created', 'modified',)



class ProfileInlie(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'



class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInlie,)
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)