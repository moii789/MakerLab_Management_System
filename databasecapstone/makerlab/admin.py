from django.contrib import admin
from .models import Item, RegisteredUser, InUseItem, EntryExit, Supervisor, Vendor

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display= ('item_name', 'quantity', 'vendor', 'warranty')

class RegisteredUserAdmin(admin.ModelAdmin):
    list_display= ('user_id', 'first_name', 'last_name', 'date_of_birth', 'email','visitor_type','student_id')

class InUseItemAdmin(admin.ModelAdmin):
    list_display= ('user', 'item_id', 'time_used_id')

class EntryExitAdmin(admin.ModelAdmin):
    list_display= ('user', 'entry_time', 'exit_time')

class SupervisorAdmin(admin.ModelAdmin):
    list_display= ('user', 'first_name', 'last_name', 'access_level')

class VendorAdmin(admin.ModelAdmin):
    list_display= ('vendor_name', 'city', 'state', 'zip')

admin.site.register(Item,ItemAdmin)
admin.site.register(RegisteredUser,RegisteredUserAdmin)
admin.site.register(InUseItem,InUseItemAdmin)
admin.site.register(EntryExit,EntryExitAdmin)
admin.site.register(Supervisor,SupervisorAdmin)
admin.site.register(Vendor,VendorAdmin)
