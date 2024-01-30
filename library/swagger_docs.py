from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiResponse, OpenApiExample
from drf_spectacular.types import OpenApiTypes

# Endpoints para Livarias

get_library_list_swagger = extend_schema(
    summary='Listar todas as livrarias',
    description='Retorna uma lista com todas as livrarias cadastradas',
    methods=['GET'],
    responses={
        200: OpenApiResponse(
            description="Lista de livrarias",
            examples={
                'application/json': {
                    'message': 'Lista de livrarias retornada com sucesso',
                }
            }
        ),
        404: OpenApiResponse(
            description="Livraria não encontrada",
            examples={
                'application/json': {
                    'message': 'Livraria não encontrada',
                }
            }
        ),
        500: OpenApiResponse(
            description="Erro interno",
            examples={
                'application/json': {
                    'message': 'Erro interno no servidor',
                }
            }
        )
    },
    tags=['Livrarias']
)

get_library_detail_swagger = extend_schema(
    summary='Detalhes de uma livraria',
    description='Retorna os detalhes de uma livraria específica',
    methods=['GET'],
    responses={
        200: OpenApiResponse(
            description="Detalhes da livraria",
            examples={
                'application/json': {
                    'message': 'Detalhes da livraria retornados com sucesso',
                }
            }
        ),
        404: OpenApiResponse(
            description="Livraria não encontrada",
            examples={
                'application/json': {
                    'message': 'Livraria não encontrada',
                }
            }
        ),
        500: OpenApiResponse(
            description="Erro interno",
            examples={
                'application/json': {
                    'message': 'Erro interno no servidor',
                }
            }
        )
    },
    tags=['Livrarias']
)

create_library_swagger = extend_schema(
    summary='Criar uma livraria',
    description='Cria uma nova livraria',
    methods=['POST'],
    request={
        'application/json': {
            'example': {
                'name': 'Livraria Saraiva',
                'location': 'Rua 7 de Setembro, 555',
            }
        }
    },
    responses={
        201: OpenApiResponse(
            description="Livraria criada",
            examples={
                'application/json': {
                    'message': 'Livraria criada com sucesso',
                }
            }
        ),
        400: OpenApiResponse(
            description="Erro de validação",
            examples={
                'application/json': {
                    'message': 'Erro de validação',
                }
            }
        ),
        500: OpenApiResponse(
            description="Erro interno",
            examples={
                'application/json': {
                    'message': 'Erro interno no servidor',
                }
            }
        )
    },
    tags=['Livrarias']
)

update_library_swagger = extend_schema(
    summary='Atualizar uma livraria',
    description='Atualiza os dados de uma livraria específica',
    methods=['PUT'],
    request={
        'application/json': {
            'example': {
                'name': 'Livraria Saraiva (atualizada)',
                'location': 'Rua Doe John, 321',
            }
        }
    },
    responses={
        200: OpenApiResponse(
            description="Livraria atualizada",
            examples={
                'application/json': {
                    'message': 'Livraria atualizada com sucesso',
                }
            }
        ),
        400: OpenApiResponse(
            description="Erro de validação",
            examples={
                'application/json': {
                    'message': 'Erro de validação',
                }
            }
        ),
        404: OpenApiResponse(
            description="Livraria não encontrada",
            examples={
                'application/json': {
                    'message': 'Livraria não encontrada',
                }
            }
        ),
        500: OpenApiResponse(
            description="Erro interno",
            examples={
                'application/json': {
                    'message': 'Erro interno no servidor',
                }
            }
        )
    },
    tags=['Livrarias']
)

# Upload de arquivos

upload_multiple_files_swagger = extend_schema(
    summary='Upload de múltiplos arquivos',
    description='Realiza o upload de múltiplos arquivos',
    methods=['POST'],
    operation_id='upload_file',
    request={
        'multipart/form-data': {
            'type': 'object',
            'properties': {
                'files': {
                    'type': 'array',
                    'items': {
                        'type': 'string',
                        'format': 'binary'
                    }
                }
            }
        }
    },
    responses={
        201: OpenApiResponse(
            description="Arquivos lidos com sucesso",
            examples={
                'application/json': {
                    'message': 'Arquivos lidos com sucesso',
                }
            }
        ),
        400: OpenApiResponse(
            description="Erro de validação",
            examples={
                'application/json': {
                    'error': 'Erro de validação',
                }
            }
        ),
        500: OpenApiResponse(
            description="Erro interno",
            examples={
                'application/json': {
                    'error': 'Erro interno no servidor',
                }
            }
        )
    },
    tags=['Arquivos']
)
