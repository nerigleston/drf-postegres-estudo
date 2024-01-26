from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample, OpenApiResponse
from drf_spectacular.types import OpenApiTypes

# Signup Swagger
signup_swagger = extend_schema(
    summary="Registrar um novo usuário",
    description="Crie um novo usuário fornecendo um nome de usuário, senha e endereço de e-mail.",
    methods=['POST'],
    request={
        'application/json': {
            'example': {
                'email': 'neris@email.com',
                'username': 'neris',
                'password': 'neris123',
            }
        }
    },
    responses={
        201: OpenApiResponse(
            description='Usuário criado com sucesso',
            examples={
                'application/json': {
                    'message': 'Usuário criado com sucesso'
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
    tags=["Authentication"],
)

# Login Swagger
login_swagger = extend_schema(
    summary="Autenticar um usuário",
    description="Realize a autenticação de um usuário fornecendo um nome de usuário e senha.",
    methods=['POST'],
    request={
        'application/json': {
            'example': {
                'username': 'neris',
                'password': 'neris123',
            }
        }
    },
    responses={
        200: OpenApiResponse(
            description='Login realizado com sucesso',
            examples={
                'application/json': {
                    'message': 'Login realizado com sucesso'
                }
            }
        ),
        404: OpenApiResponse(
            description='Usuário não encontrado',
            examples={
                'application/json': {
                    'detail': 'Usuário não encontrado'
                }
            }
        ),
    },
    tags=["Authentication"],
)

# Test Token Swagger
test_token_swagger = extend_schema(
    summary="Verificar a validade do token",
    description="Verifique se um token de autenticação é válido.",
    methods=['GET'],
    responses={
        200: OpenApiResponse(
            description='Token válido',
            examples={
                'application/json': {
                    'message': 'Token válido'
                }
            }
        ),
        401: OpenApiResponse(
            description='Token inválido',
            examples={
                'application/json': {
                    'detail': 'Token inválido'
                }
            }
        ),
    },
    tags=["Authentication"],
)


# Logout Swagger
logout_swagger = extend_schema(
    summary="Encerrar a sessão do usuário",
    description="Encerre a sessão de um usuário fornecendo o token de autenticação.",
    methods=['POST'],
    responses={
        200: OpenApiResponse(
            description='Logout realizado com sucesso',
            examples={
                'application/json': {
                    'message': 'Logout realizado com sucesso'
                }
            }
        ),
    },
    tags=["Authentication"],
)
