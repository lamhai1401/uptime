"""
User model views
"""
from django.views.generic import TemplateView
from rest_auth.views import LogoutView
from rest_framework import authentication, permissions, status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# from .models import User
from .serializers import UserSerializer


class HomeTemplateView(TemplateView):
    template_name = "home.html"


class TestAuthView(APIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):  # pylint: disable=W0622
        return Response(f"Hello {request.user}!")


class LogoutViewEx(LogoutView):
    authentication_classes = (authentication.TokenAuthentication,)


class RegisterView(GenericAPIView):
    """
    RegisterView handle user register
    """

    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # serializer.validated_data['password'] =
            #  make_password(serializer.validated_data['password'])
            user = serializer.save()
            return Response(f"Register success {user}", status=status.HTTP_201_CREATED)
        return Response(
            {
                "error_message": "This email has already exist!",
                "errors_code": 400,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
