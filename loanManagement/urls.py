from django.urls import path
from .views import HelloView, BankSerializerView, BranchSerializerView, ApplicationSerializerView,PostApplicationSerializerView, ApplicationSerializerForBranchView, ApplicationSerializerForBankView, BankSerializerWithBranchView, BankCreateSerializerView, BranchCreateSerializerView, UserInfoView, RetriveApplicationForBankView, SearchApplicationForUserView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('hello/', HelloView.as_view(), name='hello'),
    path('userinfo/', UserInfoView.as_view(), name='userInfo'),
    path('createbank/', BankCreateSerializerView.as_view(), name='create_bank'),
    path('banklist/', BankSerializerView.as_view(), name='bankList'),
    path('bankwithbranch/<str:bankname>/', BankSerializerWithBranchView.as_view(), name='BankWithBranch'),
    path('createbranch/', BranchCreateSerializerView.as_view(), name='create_branch'),
    path('branchlist/<str:bankname>/', BranchSerializerView.as_view(), name='bankList'),
    path('applicationlist/', ApplicationSerializerView.as_view(), name='applicationlist'),
    path('postapplication/', PostApplicationSerializerView.as_view(), name='postapplication'),
    path('applicationforbank/<str:preferredbank>/', ApplicationSerializerForBankView.as_view(), name='applicationForBank'),
    path('applicationforbranch/<str:preferredbranch>/', ApplicationSerializerForBranchView.as_view(), name='applicationForBank'),
    path('application/<int:pk>/', RetriveApplicationForBankView.as_view(), name='retriveApplication'),
    path('searchapplication/<str:loanId>/', SearchApplicationForUserView.as_view(), name='retriveApplication'),
]