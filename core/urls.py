from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path
from doctors.views import DoctorsListView, DoctorDetailView, KayaChatAssistantView


urlpatterns = [
    path('admin/', admin.site.urls),

    path('medicos/', DoctorsListView.as_view(), name='doctors_list'),
    path('medico/<int:pk>/', DoctorDetailView.as_view(), name='doctor_detail'),
    path('chat/', KayaChatAssistantView.as_view(), name='chat_assistant'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
