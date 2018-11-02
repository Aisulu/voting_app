from django.conf.urls import url

from . import views

#app_name = "emotions"

urlpatterns = [
               url(r'^$', views.index, name='index'),
               url(r'^vote.html$', views.vote, name='vote'),
               #url(r'^evaluate.html$', views.evaluate, name='evaluate'),
               url(r'^logout_view.html$', views.logout_view, name='logout_view'),
               #url(r'^(?P<question_id>[0-9]+)/evaluate/$', views.evaluate, name='evaluate'),
               url(r'^(?P<first_unvoted_tweet_id>[0-9]+)/$', views.evaluate, name='evaluate'),
               url(r'^delete_(?P<first_unvoted_tweet_id>[0-9]+)/$', views.delete, name='delete')
               ]
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
