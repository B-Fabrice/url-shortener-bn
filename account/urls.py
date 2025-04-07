from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from account.views import create_account, Login, logout

urlpatterns = [
    path('register/', create_account, name='create_account'),
    path('login/', Login.as_view(), name='sign-in'),
    path('logout/', logout, name='sign-out'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]