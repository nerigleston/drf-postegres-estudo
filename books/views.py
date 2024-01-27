from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import AuthorSerializer, BookSerializer
from .models import Author, Book
from .swagger_docs import (
    author_list_swagger,
    create_author_swagger,
    get_author_detail_swagger,
    update_author_swagger,
    delete_author_swagger,
    get_book_list_swagger,
    create_book_swagger,
    get_book_detail_swagger,
    update_book_swagger,
    delete_book_swagger,
    filter_book_date_swagger,
    filter_book_daterange_swagger
)

import logging
logger = logging.getLogger(__name__)

# Funções Autores


# Lista de Autores
@author_list_swagger
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_author_list(request):
    try:
        authors = Author.objects.all().order_by('name')

        if not authors:
            logger.warning('Nenhum autor encontrado ou adicionado.')
            return Response({'error': 'Nenhum autor encontrado ou adicionado'}, status=status.HTTP_404_NOT_FOUND)

        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        logger.exception(f'Erro ao obter a lista de autores: {str(e)}')
        return Response({'error': f'Erro ao obter a lista de autores: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@create_author_swagger
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_author(request):
    try:
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f'Autor criado com sucesso: {serializer.data}')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(
            f'Erro ao criar autor. Erros de validação: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.exception(f'Erro ao criar autor: {str(e)}')
        return Response({'error': f'Erro ao criar autor: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@get_author_detail_swagger
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_author_detail(request, pk):
    try:
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author)
        logger.info(
            f'Detalhes do autor obtidos com sucesso: {serializer.data}')
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Author.DoesNotExist:
        logger.warning(f'Autor não encontrado com ID {pk}')
        return Response({'error': 'Autor não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.exception(f'Erro ao obter detalhes do autor: {str(e)}')
        return Response({'error': f'Erro ao obter detalhes do autor: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@update_author_swagger
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_author(request, pk):
    try:
        author = Author.objects.get(pk=pk)
        serializer = AuthorSerializer(author, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f'Autor atualizado com sucesso: {serializer.data}')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(
            f'Erro ao atualizar autor. Erros de validação: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Author.DoesNotExist:
        logger.warning(f'Autor não encontrado com ID {pk}')
        return Response({'error': f'Autor não encontrado com ID {pk}'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.exception(f'Erro ao atualizar autor: {str(e)}')
        return Response({'error': f'Erro ao atualizar autor: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@delete_author_swagger
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_author(request, pk):
    try:
        author = Author.objects.get(pk=pk)
        author.delete()
        logger.info(f'Autor excluído com sucesso: ID {pk}')
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Author.DoesNotExist:
        logger.warning(f'Autor não encontrado com ID {pk}')
        return Response({'error': f'Autor não encontrado com ID {pk}'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.exception(f'Erro ao excluir autor: {str(e)}')
        return Response({'error': f'Erro ao excluir autor: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Funções Livros


@get_book_list_swagger
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_book_list(request):
    try:
        books = Book.objects.all()
        if not books:
            logger.warning('Nenhum livro encontrado ou adicionado.')
            return Response({'error': 'Nenhum livro encontrado ou adicionado'}, status=status.HTTP_404_NOT_FOUND)
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        logger.exception(f'Erro ao obter a lista de livros: {str(e)}')
        return Response({'error': f'Erro ao obter a lista de livros: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@create_book_swagger
@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_book(request):
    try:
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f'Livro criado com sucesso: {serializer.data}')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(
            f'Erro ao criar livro. Erros de validação: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.exception(f'Erro ao criar livro: {str(e)}')
        return Response({'error': f'Erro ao criar livro: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@get_book_detail_swagger
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_book_detail(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book)
        logger.info(
            f'Detalhes do livro obtidos com sucesso: {serializer.data}')
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Book.DoesNotExist:
        logger.warning(f'Livro não encontrado com ID {pk}')
        return Response({'error': 'Livro não encontrado'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.exception(f'Erro ao obter detalhes do livro: {str(e)}')
        return Response({'error': f'Erro ao obter detalhes do livro: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@update_book_swagger
@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            logger.info(f'Livro atualizado com sucesso: {serializer.data}')
            return Response(serializer.data, status=status.HTTP_200_OK)
        logger.error(
            f'Erro ao atualizar livro. Erros de validação: {serializer.errors}')
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Book.DoesNotExist:
        logger.warning(f'Livro não encontrado com ID {pk}')
        return Response({'error': f'Livro não encontrado com ID {pk}'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.exception(f'Erro ao atualizar livro: {str(e)}')
        return Response({'error': f'Erro ao atualizar livro: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@delete_book_swagger
@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_book(request, pk):
    try:
        book = Book.objects.get(pk=pk)
        book.delete()
        logger.info(f'Livro excluído com sucesso: ID {pk}')
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Book.DoesNotExist:
        logger.warning(f'Livro não encontrado com ID {pk}')
        return Response({'error': f'Livro não encontrado com ID {pk}'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.exception(f'Erro ao excluir livro: {str(e)}')
        return Response({'error': f'Erro ao excluir livro: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@filter_book_date_swagger
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def filter_book_date(request):
    try:
        created_at = request.query_params.get('created_at')
        if created_at is not None:
            books = Book.objects.filter(created_at=created_at)
            serializer = BookSerializer(books, many=True)
            logger.info(
                f'Livros filtrados por data com sucesso: {serializer.data}')
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            logger.error('O parâmetro "created_at" é obrigatório.')
            return Response({'error': 'O parâmetro "created_at" é obrigatório.'}, status=status.HTTP_400_BAD_REQUEST)
    except Book.DoesNotExist:
        logger.warning('Nenhum livro encontrado.')
        return Response({'error': 'Nenhum livro encontrado.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.exception(f'Erro ao filtrar livros por data: {str(e)}')
        return Response({'error': f'Erro ao filtrar livros por data: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@filter_book_daterange_swagger
@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def filter_book_daterange(request):
    try:
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if start_date is not None and end_date is not None:
            books = Book.objects.filter(
                created_at__range=[start_date, end_date])
            serializer = BookSerializer(books, many=True)
            logger.info(
                f'Livros filtrados por intervalo de data com sucesso: {serializer.data}')
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            logger.error(
                'Os parâmetros "start_date" e "end_date" são obrigatórios.')
            return Response({'error': 'Os parâmetros "start_date" e "end_date" são obrigatórios.'}, status=status.HTTP_400_BAD_REQUEST)
    except Book.DoesNotExist:
        logger.warning('Nenhum livro encontrado.')
        return Response({'error': 'Nenhum livro encontrado.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        logger.exception(
            f'Erro ao filtrar livros por intervalo de data: {str(e)}')
        return Response({'error': f'Erro ao filtrar livros por intervalo de data: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
