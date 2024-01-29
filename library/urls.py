from django.urls import path
from .views import get_library_list, get_library_detail, create_library, update_library

urlpatterns = [
    path('', get_library_list, name='library-list'),
    path('<int:pk>/', get_library_detail, name='library-detail'),
    path('create/', create_library, name='library-create'),
    path('update/<int:pk>/', update_library, name='library-update'),
]
