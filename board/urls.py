from django.conf.urls import patterns, url

from board import views

urlpatterns = patterns('',
	# ex: /
	url(r'^$', views.index, name='index'),
	# ex: /thread/1
	url(r'^(?P<thread_id>\d+)/$', views.thread, name='thread'),
	# ex: /bloard/reply/
	url(r'^(?P<thread_id>\d+)/reply/$', views.reply, name='reply'),
	# ex: /create_thread/
	url(r'^create_thread/', views.create_thread, name='create_thread'),
)
