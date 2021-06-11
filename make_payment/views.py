from django.contrib import messages
from django.shortcuts import render,HttpResponseRedirect,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
#for payment
import requests
from sslcommerz_python.payment import SSLCSession
from decimal import Context, Decimal
import socket
from loanManagement.models import Application

def payment(request, loanId):

    store_id = 'zhopz60c055c840482'
    API_key = 'zhopz60c055c840482@ssl'
    mypayment = SSLCSession(
        sslc_is_sandbox=True, 
        sslc_store_id=store_id, 
        sslc_store_pass=API_key
    )

    status_url = request.build_absolute_uri(reverse("App_Payment:complete"))
    mypayment.set_urls(
        success_url = status_url, 
        fail_url = status_url, 
        cancel_url = status_url, 
        ipn_url = status_url
    )



    mypayment.set_product_integration(
        total_amount ='50', 
        currency = 'BDT', 
        product_category = 'Mixed', 
        product_name = 'Bag', 
        num_of_item = '2', 
        shipping_method = 'Courier', 
        product_profile = 'None'
    )

    # User Info

    mypayment.set_customer_info(
        name = 'current_user.profile.full_name', 
        email = 'current_user.email', 
        address1 = 'current_user.profile.address_1', 
        address2 = 'current_user.profile.address_1', 
        city = 'current_user.profile.city', 
        postcode = 'current_user.profile.zip_code', 
        country = 'current_user.profile.country', 
        phone = 'current_user.profile.phone',
    )

    # Shipping Info
    mypayment.set_shipping_info(
        'shipping_to=current_user.profile.full_name', 
        address = 'Tollabag', 
        city = 'dhaka', 
        postcode = '1212', 
        country = 'bangladesh'
    )

    mypayment.set_additional_values(
        value_a='cusotmer@email.com', 
        value_b='portalcustomerid', 
        value_c=loanId, 
        value_d='uuid'
        
        )

    response_data = mypayment.init_payment()
    # print(response_data)
    return redirect(response_data['GatewayPageURL'])


@csrf_exempt
def complete(request):
    if request.method =='POST' or request.method =='post':
        payment_data = request.POST
        status = payment_data['status']
        loanId = payment_data['value_c']
        # application = Application.objects.filter(loanId=loanId).update(mobileNumber='01951700178')
        # print(application)
        # application.update(mobileNumber='01951700178')
        # notification.update(is_seen=True)
        if status == "VALID":
            val_id = payment_data['val_id']
            tran_id = payment_data['tran_id']
            application = Application.objects.filter(loanId=loanId).update(transactionID=tran_id, paymentStatus='Complete')
            return redirect('https://www.facebook.com/')
        elif status =="FAILED":
            messages.success(request,f"Your Payment Failed!!Please Try Again!!")
        # print(payment_data)
    return render(request,'complete.html', context={'status':status})

