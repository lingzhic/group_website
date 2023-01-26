from django.urls import path

from . import views

app_name = 'groupweb'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('research', views.ResearchView.as_view(), name='research'),
    path('members', views.MemberView.as_view(), name='members'),
    path('publications', views.PubView.as_view(), name='publications'),
    path('opportunities', views.OppView.as_view(), name='opportunities'),
]
