from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiResponse
from drf_spectacular.types import OpenApiTypes

# Endpoints para Autores
author_list_swagger = extend_schema(
    summary="Obter a lista de autores",
    description="Recupere uma lista de todos os autores.",
    methods=['GET'],
    responses={
        200: OpenApiResponse(
            description='Lista de autores recuperada com sucesso',
            examples={
                'application/json': {
                    'message': 'Lista de autores recuperada com sucesso'
                }
            }
        ),
        404: OpenApiResponse(
            description='Autores não encontrados',
            examples={
                'application/json': {
                    'message': 'Autores não encontrados'
                }
            }
        )
    },
    tags=["Autores"]
)

create_author_swagger = extend_schema(
    summary="Criar um novo autor",
    description="Crie um novo autor com o nome e biografia fornecidos.",
    methods=['POST'],
    request={
        'application/json': {
            'example': {
                'name': 'Autor Novo',
                'bio': 'Biografia do Autor Novo',
            }
        }
    },
    responses={
        201: OpenApiResponse(
            description='Autor criado com sucesso',
            examples={
                'application/json': {
                    'message': 'Autor criado com sucesso'
                }
            }
        ),
        400: OpenApiResponse(
            description='Dados inválidos no corpo da requisição',
            examples={
                'application/json': {
                    'message': 'Dados inválidos no corpo da requisição'
                }
            }
        )
    },
    tags=["Autores"]
)

get_author_detail_swagger = extend_schema(
    summary="Obter detalhes de um autor específico",
    description="Recupere detalhes de um autor específico pelo seu ID.",
    methods=['GET'],
    responses={
        200: OpenApiResponse(
            description='Detalhes do autor recuperados com sucesso',
            examples={
                'application/json': {
                    'message': 'Detalhes do autor recuperados com sucesso'
                }
            }
        ),
        404: OpenApiResponse(
            description='Autor não encontrado',
            examples={
                'application/json': {
                    'message': 'Autor não encontrado'
                }
            }
        )
    },
    tags=["Autores"]
)

update_author_swagger = extend_schema(
    summary="Atualizar detalhes de um autor específico",
    description="Atualize detalhes de um autor específico pelo seu ID com o nome e biografia fornecidos.",
    methods=['PUT'],
    request={
        "application/json": {
            "example": {
                "name": "Autor Atualizado",
                "bio": "Biografia do Autor Atualizado"
            }
        },
    },
    responses={
        200: OpenApiResponse(
            description='Detalhes do autor atualizados com sucesso',
            examples={
                'application/json': {
                    'message': 'Detalhes do autor atualizados com sucesso'
                }
            }
        ),
        404: OpenApiResponse(
            description='Autor não encontrado',
            examples={
                'application/json': {
                    'message': 'Autor não encontrado'
                }
            }
        ),
        400: OpenApiResponse(
            description='Dados inválidos no corpo da requisição',
            examples={
                'application/json': {
                    'message': 'Dados inválidos no corpo da requisição'
                }
            }
        )
    },
    tags=["Autores"]
)

delete_author_swagger = extend_schema(
    summary="Excluir um autor específico",
    description="Exclua um autor específico pelo seu ID.",
    methods=['DELETE'],
    responses={
        204: OpenApiResponse(
            description='Autor excluído com sucesso',
            examples={
                'application/json': {
                    'message': 'Autor excluído com sucesso'
                }
            }
        ),
        404: OpenApiResponse(
            description='Autor não encontrado',
            examples={
                'application/json': {
                    'message': 'Autor não encontrado'
                }
            }
        )
    },
    tags=["Autores"]
)

# Endpoints para Livros
get_book_list_swagger = extend_schema(
    summary="Obter a lista de livros",
    description="Recupere uma lista de todos os livros.",
    methods=['GET'],
    responses={
        200: OpenApiResponse(
            description='Lista de livros recuperada com sucesso',
            examples={
                'application/json': {
                    'message': 'Lista de livros recuperada com sucesso'
                }
            }
        ),
        404: OpenApiResponse(
            description='Livros não encontrados',
            examples={
                'application/json': {
                    'message': 'Livros não encontrados'
                }
            }
        )
    },
    tags=["Livros"]
)

create_book_swagger = extend_schema(
    summary="Criar um novo livro",
    description="Crie um novo livro com o título, ID do autor e data de publicação fornecidos.",
    methods=['POST'],
    request={
        'application/json': {
            'example': {
                'title': 'Livro Novo',
                'author': 1,
                'published_date': '2022-01-25',
            }
        },
    },
    responses={
        201: OpenApiResponse(
            description='Livro criado com sucesso',
            examples={
                'application/json': {
                    'message': 'Livro criado com sucesso'
                }
            }
        ),
        400: OpenApiResponse(
            description='Dados inválidos no corpo da requisição',
            examples={
                'application/json': {
                    'message': 'Dados inválidos no corpo da requisição'
                }
            }
        )
    },
    tags=["Livros"]
)

get_book_detail_swagger = extend_schema(
    summary="Obter detalhes de um livro específico",
    description="Recupere detalhes de um livro específico pelo seu ID.",
    methods=['GET'],
    responses={
        200: OpenApiResponse(
            description='Detalhes do livro recuperados com sucesso',
            examples={
                'application/json': {
                    'message': 'Detalhes do livro recuperados com sucesso'
                }
            }
        ),
        404: OpenApiResponse(
            description='Livro não encontrado',
            examples={
                'application/json': {
                    'message': 'Livro não encontrado'
                }
            }
        )
    },
    tags=["Livros"]
)

update_book_swagger = extend_schema(
    summary="Atualizar detalhes de um livro específico",
    description="Atualize detalhes de um livro específico pelo seu ID com o título, ID do autor e data de publicação fornecidos.",
    methods=['PUT'],
    request={
        "application/json": {
            "example": {
                "title": "Livro Atualizado",
                "author": 1,
                "published_date": "2022-01-25"
            }
        },
    },
    responses={
        200: OpenApiResponse(
            description='Detalhes do livro atualizados com sucesso',
            examples={
                'application/json': {
                    'message': 'Detalhes do livro atualizados com sucesso'
                }
            }
        ),
        404: OpenApiResponse(
            description='Livro não encontrado',
            examples={
                'application/json': {
                    'message': 'Livro não encontrado'
                }
            }
        ),
        400: OpenApiResponse(
            description='Dados inválidos no corpo da requisição',
            examples={
                'application/json': {
                    'message': 'Dados inválidos no corpo da requisição'
                }
            }
        )
    },
    tags=["Livros"]
)

delete_book_swagger = extend_schema(
    summary="Excluir um livro específico",
    description="Exclua um livro específico pelo seu ID.",
    methods=['DELETE'],
    responses={
        204: OpenApiResponse(
            description='Livro excluído com sucesso',
            examples={
                'application/json': {
                    'message': 'Livro excluído com sucesso'
                }
            }
        ),
        404: OpenApiResponse(
            description='Livro não encontrado',
            examples={
                'application/json': {
                    'message': 'Livro não encontrado'
                }
            }
        )
    },
    tags=["Livros"]
)
