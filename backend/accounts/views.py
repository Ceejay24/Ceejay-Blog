from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions

class SignupView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data

        username = data['username']
        email = data['email']
        password = data['password']
        password2 = data['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email is already registered'})
            
            else:
                if len(password) < 6:
                    return Response({'error': 'Password must not be less than 6 characters'})

                else:
                    user = User.objects.create_user(email=email, password=password, username=username)

                    user.save()
                    return Response({'success': 'User created successfully'})

        else:
            return Response({'error': 'Passwords do not match'})