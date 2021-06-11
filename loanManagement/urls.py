from django.urls import path
from .views import HelloView, BankSerializerView, BranchSerializerView, ApplicationSerializerView,PostApplicationSerializerView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('banklist/', BankSerializerView.as_view(), name='bankList'),
    path('branchlist/', BranchSerializerView.as_view(), name='bankList'),
    path('applicationlist/', ApplicationSerializerView.as_view(), name='applicationlist'),
    path('postapplication/', PostApplicationSerializerView.as_view(), name='postapplication'),
    # path('postapplication/', csrf_exempt(postApplicationSerializerView), name='postapplication'),
]