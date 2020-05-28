from django.urls import path
from account.api.views import (
    registration_view,
    account_properties_view,
    update_account_view,
    ObtainAuthTokenView,
    does_account_exist_view,
    ChangePasswordView,
)

# looks for user model at settings
# from rest_framework.authtoken.views import obtain_auth_token

app_name = 'account'

urlpatterns = [
    path('check_if_account_exists/', does_account_exist_view,
         name="check_if_account_exists"),
    path('change_password/', ChangePasswordView.as_view(), name="change_password"),
    path('login', ObtainAuthTokenView.as_view(), name='login'),
    # path('login', obtain_auth_token, name='login'),
    path('properties', account_properties_view, name='properties'),
    path('properties/update', update_account_view, name='update'),
    path('register', registration_view, name='register'),
]
