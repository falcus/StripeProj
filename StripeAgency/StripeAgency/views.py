from django.shortcuts import render
from django.shortcuts import render
import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from payment.forms import PaymentForm

def index(request):
    return render(request, 'index.html')

stripe.api_key = settings.STRIPE_SECRET_KEY

def process_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            try:
                charge = stripe.Charge.create(
                    amount=1000,
                    currency='usd',
                    source=request.POST['stripeToken'],
                    description='Example charge'
                )
                # If the charge is successful, redirect to a success page
                return redirect('payment_success')
            except stripe.error.CardError as e:
                # If there's an error with the user's card, display an error message
                form.add_error(None, e.error.message)
    else:
        form = PaymentForm()
    return render(request, 'process_payment.html', {'form': form})