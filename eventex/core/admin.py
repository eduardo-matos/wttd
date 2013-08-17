from django.contrib import admin
from eventex.core.models import Contact, Speaker, Talk, Media

class ContactInline(admin.TabularInline):
    model = Contact
    extra = 1

class MediaInline(admin.TabularInline):
    model = Media
    etra = 1

class SpeakerAdmin(admin.ModelAdmin):
    inlines = [ContactInline,]
    prepopulated_fields = {'slug': ('name',)}

class TalkAdmin(admin.ModelAdmin):
    inlines = [MediaInline,]

admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Talk, TalkAdmin)