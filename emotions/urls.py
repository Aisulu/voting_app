from django.conf.urls import url

from . import views

urlpatterns = [
               url(r'^$', views.index, name='index'),
               url(r'^vote.html$', views.vote, name='vote'),
               url(r'^logout_view.html$', views.logout_view, name='logout_view'),
               url(r'^(?P<first_unvoted_tweet_id>[0-9]+)/$', views.evaluate, name='evaluate'),
               ]
