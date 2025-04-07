from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from account.serializers import RegistrationSerializer, LoginSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth.models import User

@api_view(['POST'])
def create_account(request: Request):
    serializer = RegistrationSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    user = serializer.save()
    return Response(
        {"username": user.username, "email": user.email},
        status=status.HTTP_201_CREATED
    )

class Login(TokenObtainPairView):
    serializer_class = LoginSerializer
    
    def post(self, request: Request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        if not email or not password:
            return Response(
                {"error": "Email and password are required."},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {"error": "Invalid email or password."},
                status=status.HTTP_401_UNAUTHORIZED
            )
        
        try:
            request.data._mutable = True
        except AttributeError:
            pass
        request.data['username'] = user.username
        return super().post(request, *args, **kwargs)