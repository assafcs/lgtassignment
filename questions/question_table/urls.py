from django.conf.urls import patterns, url

from question_table import views

urlpatterns = patterns('',
    url(r'^$', views.questions_view, name='questions view'),
    url(r'^api$', views.question_list, name='question list'),
    url(r'^api/(?P<pk>\d+)/$', views.question_detail, name="question details"),
)
