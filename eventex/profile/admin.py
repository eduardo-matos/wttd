from django.contrib.auth import get_user_model
from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin 
from eventex.profile.models import Profile


_User = get_user_model()

class ProfileInline(admin.StackedInline):
	model = Profile
	can_delete = False


class UserAdmin(UserAdmin):
	inlines = (ProfileInline,)

admin.site.unregister(_User)
admin.site.register(_User, UserAdmin)