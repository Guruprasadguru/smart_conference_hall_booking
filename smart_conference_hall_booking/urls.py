"""smart_conference_hall_booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from app import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls'),name='login'),
    path('signup', views.signup),
    path('', views.home,name='home'),
    path('booking/<id>', views.booking,name='order'),
    path('myprofile', views.myprofile,name='myprofile'),
    path('update/<id>', views.update,name='update'),
    path('subscription/', views.subscription,name='subscription'),
    path('payment/', views.payment,name='payment'),
    path('paymentdetail/', views.paymentdetail,name='paymentdetail'),
    path('cancel/', views.cancel,name='cancel')
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
