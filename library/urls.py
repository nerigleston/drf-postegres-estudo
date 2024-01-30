from django.urls import path
from django.conf.urls.static import static
from postegresRelacao import settings
from .views import get_library_list, get_library_detail, create_library, update_library, upload_multiple_files

urlpatterns = [
    path('', get_library_list, name='library-list'),
    path('<int:pk>/', get_library_detail, name='library-detail'),
    path('create/', create_library, name='library-create'),
    path('update/<int:pk>/', update_library, name='library-update'),

    path('upload/', upload_multiple_files, name='file-upload'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
