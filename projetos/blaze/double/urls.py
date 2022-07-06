from django.urls import	URLPattern, path
from .views import ListaDoubleView

urlpatterns = [
    path('', ListaDoubleView.as_view(), name='double.index')
]