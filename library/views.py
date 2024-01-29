import logging
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import LibrarySerializer
from .models import Library
from .swagger_docs import (
    get_library_list_swagger,
    get_library_detail_swagger,
    create_library_swagger,
    update_library_swagger,
)

logger = logging.getLogger(__name__)


@get_library_list_swagger
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_library_list(request):
    try:
        libraries = Library.objects.all().order_by('name')
        serializer = LibrarySerializer(libraries, many=True)
        logger.info('Lista de bibliotecas recuperada com sucesso.')
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f'Erro ao recuperar lista de bibliotecas: {str(e)}')
        return Response({'error': 'Erro interno do servidor'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@get_library_detail_swagger
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_library_detail(request, pk):
    try:
        library = Library.objects.get(pk=pk)
        serializer = LibrarySerializer(library)
        logger.info(
            f'Detalhes da biblioteca com ID {pk} recuperados com sucesso.')
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Library.DoesNotExist:
        logger.warning(f'Livraria não encontrada com ID {pk}.')
        return Response({'error': f'Livraria não encontrada com ID {pk}'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(f'Erro ao recuperar detalhes da biblioteca: {str(e)}')
        return Response({'error': 'Erro interno do servidor'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@create_library_swagger
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_library(request):
    try:
        serializer = LibrarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info('Biblioteca criada com sucesso.')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(f'Erro ao criar biblioteca: {str(e)}')
        return Response({'error': 'Erro interno do servidor'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@update_library_swagger
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_library(request, pk):
    try:
        library = Library.objects.get(pk=pk)
        serializer = LibrarySerializer(
            library, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            logger.info(f'Biblioteca com ID {pk} atualizada com sucesso.')
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Library.DoesNotExist:
        logger.warning(f'Livraria não encontrada com ID {pk}.')
        return Response({'error': f'Livraria não encontrada com ID {pk}'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.error(f'Erro ao atualizar biblioteca: {str(e)}')
        return Response({'error': 'Erro interno do servidor'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
