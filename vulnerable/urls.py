from django.urls import path, re_path

from .views import views
from .views import code
from .views import commands
from .views import sql_injection

urlpatterns = [
    path('about/', views.AboutView.as_view(), name='about'),
    re_path('about/(?P<path>[\w\./]+)$', views.AboutView.as_view(), name='files'),
    path('list/', views.VulnerabilitiesListView.as_view(), name='list'),
    path('sql/basic', sql_injection.BasicView.as_view(), name='sql_basic'),
    path('sql/extra/where', sql_injection.ExtraWhereView.as_view(), name='sql_extra_where'),
    path('command', commands.CommandsView.as_view(), name='command_basic'),
    path('code', code.CodeView.as_view(), name='code_basic'),
]
