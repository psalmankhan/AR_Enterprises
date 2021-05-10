from django.shortcuts import render, redirect
from .models import Order, Contact
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        total = request.POST.get('total')
        brand = request.POST.get('brand')

        order_form = Order(name=name, email=email, phone=phone,
                            total=total, brand=brand)

        # admin_info = User.objects.get(is_superuser=True)
        # admin_email = admin_info.email

        # send_mail(
        #     subject='Order Received',
        #     message='You received an order. Please check admin section',
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=[admin_email],
        #     fail_silently=False,
        # )
        order_form.save()
        messages.success(request, 'Your order request has been submitted successfully. We will get back you shortly')
    return render(request, 'order.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact_form = Contact(name=name, email=email, message=message)

        # admin_info = User.objects.get(is_superuser=True)
        # admin_email = admin_info.email

        # send_mail(
        #     subject='Enquiry',
        #     message='You received a message. Please check admin section',
        #     from_email=settings.EMAIL_HOST_USER,
        #     recipient_list=[admin_email],
        #     fail_silently=False,
        # )

        contact_form.save()

        messages.success(request, 'Your message has been submitted successfully. We will get back you shortly')
    return render(request, 'contact.html')
