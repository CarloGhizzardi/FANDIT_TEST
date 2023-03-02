from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models import User

class RegisterUserView(APIView):
    def post(self, request):
        pass
