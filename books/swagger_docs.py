from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse, OpenApiExample
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
                    'message': 'Nenhum autor encontrado ou adicionado'
                }
            }
        ),
        500: OpenApiResponse(
            description='Erro interno no servidor',
            examples={
                'application/json': {
                    'message': 'Erro interno no servidor'
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
        ),
        500: OpenApiResponse(
            description='Erro interno no servidor',
            examples={
                'application/json': {
                    'message': 'Erro interno no servidor'
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
        ),
        500: OpenApiResponse(
            description='Erro interno no servidor',
            examples={
                'application/json': {
                    'message': 'Erro interno no servidor'
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
        ),
        500: OpenApiResponse(
            description='Erro interno no servidor',
            examples={
                'application/json': {
                    'message': 'Erro interno no servidor'
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
        ),
        500: OpenApiResponse(
            description='Erro interno no servidor',
            examples={
                'application/json': {
                    'message': 'Erro interno no servidor'
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
                    'message': 'Nenhum livro encontrado ou adicionado'
                }
            }
        ),
        500: OpenApiResponse(
            description='Erro interno no servidor',
            examples={
                'application/json': {
                    'message': 'Erro interno no servidor'
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
                'created_at': '2020-01-25',
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
        ),
        500: OpenApiResponse(
            description='Erro interno no servidor',
            examples={
                'application/json': {
                    'message': 'Erro interno no servidor'
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
        ),
        500: OpenApiResponse(
            description='Erro interno no servidor',
            examples={
                'application/json': {
                    'message': 'Erro interno no servidor'
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
        ),
        500: OpenApiResponse(
            description='Erro interno no servidor',
            examples={
                'application/json': {
                    'message': 'Erro interno no servidor'
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
        ),
        500: OpenApiResponse(
            description='Erro interno no servidor',
            examples={
                'application/json': {
                    'message': 'Erro interno no servidor'
                }
            }
        )
    },
    tags=["Livros"]
)

filter_book_date_swagger = extend_schema(
    summary="Filtrar livros por data de criação",
    description="Filtre livros por data de criação.",
    methods=['GET'],
    parameters=[
        OpenApiParameter(
            name='created_at',
            description='Data de criação - EX: 2020-01-25',
            required=True,
            type=OpenApiTypes.DATE,
            location=OpenApiParameter.QUERY,
        ),
    ],
    responses={
        200: OpenApiResponse(
            description='Livros filtrados com sucesso',
            examples={
                'application/json': {
                    'message': 'Livros filtrados com sucesso'
                }
            }
        ),
        400: OpenApiResponse(
            description='Parâmetro "created_at" não informado',
            examples={
                'application/json': {
                    'message': 'Parâmetro "created_at" não informado'
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
        ),
        500: OpenApiResponse(
            description='Erro interno no servidor',
            examples={
                'application/json': {
                    'message': 'Erro interno no servidor'
                }
            }
        )
    },
    tags=["Livros"]
)

filter_book_daterange_swagger = extend_schema(
    summary="Filtrar livros por intervalo de datas de criação",
    description="Filtre livros por intervalo de datas de criação.",
    methods=['GET'],
    parameters=[
        OpenApiParameter(
            name='start_date',
            description='Data de criação inicial - EX: 2020-01-25',
            required=True,
            type=OpenApiTypes.DATE,
            location=OpenApiParameter.QUERY,
        ),
        OpenApiParameter(
            name='end_date',
            description='Data de criação final - EX: 2022-01-25',
            required=True,
            type=OpenApiTypes.DATE,
            location=OpenApiParameter.QUERY,
        ),
    ],
    responses={
        200: OpenApiResponse(
            description='Livros filtrados com sucesso',
            examples={
                'application/json': {
                    'message': 'Livros filtrados com sucesso'
                }
            }
        ),
        400: OpenApiResponse(
            description='Parâmetros "start_date" e "end_date" não informados',
            examples={
                'application/json': {
                    'message': 'Parâmetros "start_date" e "end_date" não informados'
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
        ),
        500: OpenApiResponse(
            description='Erro interno no servidor',
            examples={
                'application/json': {
                    'message': 'Erro interno no servidor'
                }
            }
        )
    },
    tags=["Livros"]
)
