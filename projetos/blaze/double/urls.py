from django.urls import	URLPattern, path
from .views import DoubleCreateView, ListaDoubleView, DoubleUpdateView, DoubleDeleteView

urlpatterns = [
    path('', ListaDoubleView.as_view(), name='double.index'),
    path('novo/', DoubleCreateView.as_view(), name='double.novo'),
    path('editar/<int:pk>', DoubleUpdateView.as_view(), name='double.editar'),
    path('remover/<int:pk>', DoubleDeleteView.as_view(), name='double.remover')
]
