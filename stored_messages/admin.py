from django.contrib import admin
from .models import Inbox, Message, MessageArchive

# todo: raw ID fields.

admin.site.register(Inbox)
admin.site.register(Message)
class MessageAdmin(admin.ModelAdmin):
    '''
        Admin View for Message
    '''
    raw_id_fields = ('sender', 'thread',)
    readonly_fields = ('',)
    search_fields = ['sender']

admin.site.register(Message, MessageAdmin)
admin.site.register(MessageArchive)