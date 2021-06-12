from .views import payment, complete
from django.urls import path


app_name="App_Payment"

urlpatterns = [
    path('pay/<str:loanId>/', payment, name='payment'),
    path('status/', complete, name='complete'),


]
