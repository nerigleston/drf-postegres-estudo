from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import ProfileUserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .swagger_docs import signup_swagger, login_swagger, test_token_swagger, logout_swagger
from datetime import timedelta

# Signup View


@signup_swagger
@api_view(['POST'])
def signup(request):
    serializer = ProfileUserSerializer(data=request.data)
    if serializer.is_valid():
        user = User.objects.create_user(
            username=serializer.validated_data['username'])
        user.set_password(serializer.validated_data['password'])
        user.save()
        refresh = RefreshToken.for_user(user)
        refresh.access_token.set_exp(lifetime=timedelta(hours=1))
        access_token = str(refresh.access_token)
        return Response({'token': 'Bearer ' + access_token, 'user': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Login View


@login_swagger
@api_view(['POST'])
def login(request):
    try:
        username = request.data.get('username', '')
        user = User.objects.get(username=username)
        refresh = RefreshToken.for_user(user)
        refresh.access_token.set_exp(lifetime=timedelta(hours=1))
        access_token = str(refresh.access_token)
        serializer = ProfileUserSerializer(user)

        return Response({'token': 'Bearer ' + access_token, 'user': serializer.data}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Test Token View


@test_token_swagger
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_token(request):
    user = request.user
    return Response("Token válido para o usuário {}".format(user.username), status=status.HTTP_200_OK)

# Logout View


@logout_swagger
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    request.auth.delete()
    return Response("Logout realizado com sucesso", status=status.HTTP_200_OK)
