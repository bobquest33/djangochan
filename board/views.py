from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render_to_response
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.core.context_processors import csrf
from django.utils.html import conditional_escape

from board.models import Thread, Post

from random import randint
import re

# Create your views here.
def index(request, page_number=None):
	# Get all threads
	threads = Thread.objects.all()

	# Get the thread count so pages can be made
	threadcount = threads.count()

	# Get the most recently created 15 threads
	if page_number:
		start = int(page_number) * 15
		# Check if start is less than total threads
		if start < threadcount:
			end = start+15 if start+15 < threadcount else threadcount
			recentthreads = threads.order_by('-last_bumped')[start:end]
		else:
			recentthreads = threads.order_by('-last_bumped')[:15]
	else:
		recentthreads = threads.order_by('-last_bumped')[:15]

	# Get last 5 comments for each of the last 15 created threads
	replies = [0 for x in range(recentthreads.count())]	
	for i in range(0,recentthreads.count()):
		replies[i] = Post.objects.order_by('-pub_date').filter(thread=recentthreads[i])[:5]
		
	# Generate random numbers for simple captcha
	a = randint(0,10)
	b = randint(0,10)

	# Get number of pages
	pagecount = threadcount / 15

	d = dict(threads=recentthreads, replies=replies, a=a, b=b, threadcount=threadcount, pagenumber=page_number, pagecount=pagecount)
	d.update(csrf(request))
	return render_to_response("board/index.html", d)	

def thread(request, thread_id):
	thread = Thread.objects.get(pk=int(thread_id))
	replies = Post.objects.order_by('pub_date').filter(thread=thread)

	# Generate random numbers for simple catcha
	a = randint(0, 10)
	b = randint(0, 10)

	d = dict(thread=thread, replies=replies, a=a, b=b)
	d.update(csrf(request))
	return render_to_response("board/thread.html", d)

def create_thread(request):
	if request.method == 'POST':
		title = request.POST['title']
		text = request.POST['text']
		if len(text) > 5 and len(text) < 2000:
			# Check captcha was correct
			a = request.POST['a']
			b = request.POST['b']
			value = request.POST['captcha']
			if int(a) + int(b) == int(value or 0):		
				thread = Thread(thread_title=title, thread_text=text)
				thread.save()
	
		return HttpResponseRedirect(reverse('index')) 

def reply(request, thread_id):
	thread = get_object_or_404(Thread, pk=thread_id)
	if request.method == 'POST':
		text = request.POST['text']
		if text and len(text) > 5 and len(text) < 2000:
			# Check captcha
			a = request.POST['a']
			b = request.POST['b']
			value = request.POST['captcha']
			if int(a) + int(b) == int(value or 0):
				# Escape the html
				text = conditional_escape(text)
				post = Post(thread=thread, post_text=text)
				post.save()
				thread.thread_count += 1
				thread.save()

	return HttpResponseRedirect(reverse('thread', args=(thread.id,)))
