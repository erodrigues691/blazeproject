from django.urls import	URLPattern, path
from django.contrib.auth.decorators import login_required
from .views import DoubleCreateView, ListaDoubleView, DoubleUpdateView, DoubleDeleteView
from . import views

urlpatterns = [
    path('', ListaDoubleView.as_view(), name='double.index'),
    path('novo/', DoubleCreateView.as_view(), name='double.novo'),
    path('<int:pk>/editar', DoubleUpdateView.as_view(), name='double.editar'),
    path('<int:pk>/remover',DoubleDeleteView.as_view(), name='double.remover'),
    path('<int:pk_double>/contatos', views.Contatos, name='double.contatos'),
    path('<int:pk_double>/contato/novo/',views.contato_novo, name='contato.novo'),
    path('<int:pk_double>/contato/<int:pk>/editar',views.contato_editar, name='contato.editar'),
    path('<int:pk_double>/contato/<int:pk>/remover',views.contato_remover, name='contato.remover'),
]
