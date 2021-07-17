from django.urls import path

from .views import index, by_rubric, test
from .views import BbCreateView

urlpatterns = [
    path('test/', test, name='test'),
    path('add/', BbCreateView.as_view(), name='add'),
    path('<int:rubric_id>/', by_rubric, name='by_rubric'),
    path('', index, name='index'),
]