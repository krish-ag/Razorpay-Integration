from django.shortcuts import render, HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
def home(request):
    # if request.method == "POST":
    data = {"amount": 500 * 100, "currency": "INR"}
    payment = settings.client.order.create(data=data)
    print(payment)

    return render(request, 'index.html', {"payment": payment, "key": settings.RAZORPAY_KEY_ID})


@csrf_exempt
def payment(request):
    if request.method == "POST":
        params = request.POST
        verification = settings.client.utility.verify_payment_signature(params)
        return HttpResponse(str(verification))