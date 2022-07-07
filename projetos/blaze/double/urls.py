from django.urls import	URLPattern, path
from .views import DoubleCreateView, ListaDoubleView

urlpatterns = [
    path('', ListaDoubleView.as_view(), name='double.index'),
    path('novo/', DoubleCreateView.as_view(), name='double.novo')
]