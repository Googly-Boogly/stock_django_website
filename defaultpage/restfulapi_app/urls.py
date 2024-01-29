from django.urls import path
from . import views

urlpatterns = [
    path('api/mock-data/', views.get_mock_data),
    path('api/llm-interaction/', views.interact_with_llm),
    path('api/specific-function/', views.specific_function),
    path('api/process-payment/', views.process_payment),
]