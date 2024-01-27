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

import logging
logger = logging.getLogger(__name__)

# Signup View


@signup_swagger
@api_view(['POST'])
def signup(request):
    try:
        serializer = ProfileUserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email']
            )
            user.set_password(serializer.validated_data['password'])
            user.save()
            refresh = RefreshToken.for_user(user)
            refresh.access_token.set_exp(lifetime=timedelta(hours=1))
            access_token = str(refresh.access_token)
            logger.info(f"Usuário cadastrado com sucesso: {user.username}")
            return Response({'token': access_token, 'user': serializer.data}, status=status.HTTP_201_CREATED)
        else:
            logger.error(
                f"Cadastro falhou. Erros de validação: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.exception(f"Ocorreu um erro durante o cadastro: {str(e)}")
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
        logger.info(f"Usuário logado com sucesso: {user.username}")
        return Response({'token': access_token, 'user': serializer.data}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        logger.warning(f"Login falhou. Usuário não encontrado: {username}")
        return Response({'error': 'Usuário não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.exception(f"Ocorreu um erro durante o login: {str(e)}")
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Test Token View


@test_token_swagger
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_token(request):
    user = request.user
    logger.info(f"Teste de token bem-sucedido para o usuário: {user.username}")
    return Response("Token válido para o usuário {}".format(user.username), status=status.HTTP_200_OK)

# Logout View


@logout_swagger
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def logout(request):
    user = request.user
    logger.info(f"Usuário desconectado com sucesso: {user.username}")
    request.auth.delete()
    return Response("Logout realizado com sucesso", status=status.HTTP_200_OK)
