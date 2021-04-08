from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from app.models import *


class Signup_form(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


class User_detail_form(forms.ModelForm):
    class Meta:
        model = User_detail
        fields = ['phone','address','branch']

#
class Booking_Form(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_date_for']
#
#
class Payment_detailForm(forms.ModelForm):
    class Meta:
        model = Payment_detail
        fields= ['payment_screenshot']


