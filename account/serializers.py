from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class RegistrationSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        required=False,
        allow_blank=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="That username is already taken."
            )
        ]
    )

    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="That email is already registered."
            )
        ]
    )

    password  = serializers.CharField(
        write_only=True,
        required=True,
        min_length=6,
        error_messages={
            'min_length': 'Password must be 6 character minimum'
        }
    )

    class Meta:
        model  = User
        fields = ('username', 'email', 'password')

    def validate(self, attrs):
        if not attrs.get('username'):
            attrs['username'] = attrs['email']

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class UserSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(source='date_joined', read_only=True)

    class Meta:
        model  = User
        fields = ('username', 'email', 'created_at')


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        tokens = super().validate(attrs)
        serializer = UserSerializer(self.user)
        return {
            'tokens': tokens,
            'user': serializer.data
        }
