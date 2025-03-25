import json
from django.http import JsonResponse
from django.db.models import Q
from doctors.models import Specialty, Doctor
from django.views.generic import View, ListView, DetailView
from services.ia.assistant import KayaAssistantAI


class DoctorsListView(ListView):
    model = Doctor
    template_name = 'doctors/doctors_list.html'
    context_object_name = 'doctors'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        search = self.request.GET.get('search')
        specialty = self.request.GET.get('specialty')
        order = self.request.GET.get('order')

        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) | Q(specialty__name__icontains=search)
            )
        if specialty:
            queryset = queryset.filter(specialty__id=specialty)
        
        if order == 'asc':
            queryset = queryset.order_by('value')
        if order == 'desc':
            queryset = queryset.order_by('-value')
        
        return queryset
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['specialties'] = Specialty.objects.all().order_by('name')
        specialty_id = self.request.GET.get('specialty')
        
        if specialty_id:
            context['selected_specialty'] = Specialty.objects.get(id=specialty_id)
        else:
            context['selected_specialty'] = None
        
        return context


class DoctorDetailView(DetailView):
    model = Doctor
    template_name = 'doctors/doctor_detail.html'


class KayaChatAssistantView(View):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.chat_ia = KayaAssistantAI()
    

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")

            if not user_message:
                return JsonResponse({"error": "Mensagem vazia"}, status=400)

            response = self.chat_ia.to_ask(question=user_message)

            return JsonResponse({"response": response})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
