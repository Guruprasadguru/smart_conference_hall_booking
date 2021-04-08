import uuid

from django.db import models
from django.contrib.auth.models import User



# Create your models here.


class User_detail(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True)
    address = models.CharField(max_length=200, null=True)
    branch = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user.username


class Conference_hall_type(models.Model):
    conference_hall_name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.conference_hall_name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Booking(models.Model):
    STATUS_CHOICES1 = (('Pending', 'Pending'), ('Paid', 'Paid'))
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    conference_hall = models.ForeignKey(Conference_hall_type, on_delete=models.SET_NULL, null=True)
    booking_date_for=models.DateField(unique=True)
    date_of_booking = models.DateTimeField(auto_now=True)
    transaction_id = models.CharField(max_length=36, default=uuid.uuid4)
    payment_status = models.CharField(max_length=20, choices=STATUS_CHOICES1, default='Pending')

    def __str__(self):
        return self.user.username
    #
    # @property
    # def get_total(self):
    #     total = self.conference_hall.price
    #     return total


class Bank_detail(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    qrcode = models.ImageField(default="QRCode.png", null=True, blank=True)
    upiid = models.CharField(max_length=100, null=True, blank=True)

    @property
    def qrcodeURL(self):
        try:
            url = self.qrcode.url
        except:
            url = ''
        return url

class Payment_detail(models.Model):
    STATUS_CHOICES = (('Verified', 'Verified'), ('Not Verified', 'Not Verified'))
    user = models.ForeignKey(User,null=True, blank=True, on_delete=models.CASCADE)
    Conference_hall = models.ForeignKey(Conference_hall_type, null=True, blank=True, on_delete=models.CASCADE)
    transaction_id= models.CharField(max_length=100,null=True)
    booking_date_for=models.DateTimeField()
    total=models.FloatField(null=True)
    payment_screenshot=models.ImageField(null=True, blank=True)
    date_payment = models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=50,choices=STATUS_CHOICES,default='Not Verified')

# Create your models here.
