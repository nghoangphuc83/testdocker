from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('polls/latest.html', views.index),
    # added the word 'specifics'
	path('specifics/<int:question_id>/', views.detail, name='detail'),

    # the 'name' value as called by the {% url %} template tag
	path('<int:question_id>/', views.detail, name='detail'),


    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # detail(request=<HttpRequest object>, question_id=34),


]