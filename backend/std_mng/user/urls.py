from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import UserSignup, UserList, UserLogin

urlpatterns = [
    path('', UserList.as_view(), name='user_list'),
    path('signup/', UserSignup.as_view(), name='user_signup'),
    path('login/', UserLogin.as_view(), name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
