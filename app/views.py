
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

import app
from app.forms import *
from app.models import *


# Create your views here.
def signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = Signup_form()
        user_form = User_detail_form()

        if request.method == 'POST':
            form = Signup_form(request.POST)
            user_form = User_detail_form(request.POST)
            if form.is_valid() and user_form.is_valid():
                user = form.save()
                userdetail = user_form.save(commit=False)
                userdetail.user = user
                userdetail.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form, 'user_form': user_form}
        return render(request, 'app/signup.html', context)


# Create your views here.
@login_required
def home(request):
    products = Conference_hall_type.objects.all()

    context = {'products': products}
    return render(request, 'app/home.html', context)

@login_required
def booking(request, id):
    if request.user.is_authenticated:
        product = Conference_hall_type.objects.get(id=id)
        user=request.user

        if request.method=='POST':
            form=Booking_Form(request.POST)
            try:
                form.is_valid()
                order=form.save(commit=False)
                order.user=user
                order.conference_hall=product
                order.save()
                return redirect('payment')
            except:
                messages.success(request, 'Room Not Avelable For This Date ' )
        form=Booking_Form()
        context = {'Conference_hall': product,'form':form}
    return render(request, 'app/orderitem.html', context)

@login_required
def subscription(request):
    if request.user.is_authenticated:
        try:
            user=request.user
            orderitem=Booking.objects.filter(user=user).order_by('-date_of_booking')
            context={'orderitem':orderitem}
            return render(request,'app/subscription.html',context)
        except app.models.Booking.DoesNotExist as e:
            print(e)
            context = {}
            return render(request,'app/subscription.html',context)
@login_required
def payment(request):
    if request.user.is_authenticated:
        bank =Bank_detail.objects.all()
        user=request.user
        subscription=Booking.objects.filter(user=user,payment_status='Pending').order_by('-date_of_booking')[0]
        form=Payment_detailForm()
        if request.method == 'POST':
            form = Payment_detailForm(request.POST,request.FILES)
            if form.is_valid():
                pay=form.save(commit=False)
                pay.user=subscription.user
                pay.Conference_hall=subscription.conference_hall
                pay.transaction_id=subscription.transaction_id
                pay.total=subscription.conference_hall.price
                pay.booking_date_for=subscription.booking_date_for
                pay.save()
                return redirect('home')
        context={'form':form,'subscription':subscription,'bank':bank }
        return render(request,'app/payment.html',context)
def paymentdetail(request):
    if request.user.is_authenticated:
        user=request.user
        detail=Payment_detail.objects.filter(user=user).order_by('-date_payment')
        context={'detail':detail}
        return render(request,'app/paymentdetail.html',context)

@login_required
def cancel(request):
    if request.user.is_authenticated:
        user = request.user
        subscription = Booking.objects.filter(user=user, payment_status='Pending').order_by('-date_of_booking')[0]
        subscription.delete()
        return redirect('home')
@login_required
def myprofile(request):
    if request.user.is_authenticated:
        username = request.user.username
    context = {'username': username}
    return render(request, 'app/myprofile.html', context)



@login_required
def update(request, id):
    if request.user.is_authenticated:
        user=request.user
    emp = User_detail.objects.get(user=user,id=id)
    form = User_detail_form(instance=emp)

    if request.method == 'POST':
        form = User_detail_form(request.POST, instance=emp)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'app/update.html', {'form': form})