# gym/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Class, Payment
import stripe

def class_list(request):
    classes = Class.objects.all()
    return render(request, 'gym/class_list.html', {'classes': classes})

def book_class(request, class_id):
    selected_class = get_object_or_404(Class, pk=class_id)
    # Here you would handle the booking logic
    return render(request, 'gym/book_class.html', {'class': selected_class})

def process_payment(request):
    if request.method == 'POST':
        # Payment processing logic goes here
        return HttpResponse('Payment processed')
    return render(request, 'gym/process_payment.html')

def process_payment(request):
    if request.method == 'POST':
        token = request.POST.get('stripeToken')
        try:
            charge = stripe.Charge.create(
                amount=5000,  # $50.00
                currency='usd',
                source=token,
                description='Gym Class Payment',
            )
            Payment.objects.create(
                user=request.user,
                amount=50.00,
                payment_status='Completed',
            )
            return HttpResponse('Payment processed')
        except stripe.error.StripeError:
            return HttpResponse('Payment failed')
    return render(request, 'gym/process_payment.html')