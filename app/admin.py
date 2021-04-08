from django.contrib import admin
from app.models import *

'''Register your models here.'''


class User_detailAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'phone', 'address', 'branch', 'date_created']

#
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'user','conference_hall', 'booking_date_for', 'date_of_booking', 'transaction_id','payment_status']

class Bank_detailAdmin(admin.ModelAdmin):
    list_display = ['name','qrcode','upiid']
#
class Payment_detailAdmin(admin.ModelAdmin):
    list_display = ['user','Conference_hall','transaction_id','total','payment_screenshot','date_payment','status']
#     # ''' 'user','Conference_hall','validity','transaction_id','total' '''
#
admin.site.register(User_detail, User_detailAdmin)
admin.site.register(Conference_hall_type)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Bank_detail,Bank_detailAdmin)
admin.site.register(Payment_detail,Payment_detailAdmin)

