from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer
from .models import User


#this is just for reading all users

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserSignup(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]



from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate 


class UserLogin(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        print(f"Attempting login with email: {email}")  # Debugging info

        # Use authenticate with the custom backend
        user = authenticate(request, username=email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        print('request is', request.data)
        print(f"Failed login attempt for email: {email}")  # Debugging info
        return Response({'error': 'Invalid Credentials'}, status=status.HTTP_400_BAD_REQUEST)

