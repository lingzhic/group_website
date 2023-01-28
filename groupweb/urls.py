from django.urls import path

from . import views

app_name = 'groupweb'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('research', views.research_view, name='research'),
    # path('research', views.ResearchView.as_view(), name='research'),
    path('members', views.member_view, name='members'),
    path('publications', views.publication_view, name='publications'),
    path('opportunities', views.opportunities_view, name='opportunities'),
]
