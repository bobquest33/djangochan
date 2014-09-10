from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.core.context_processors import csrf

from board.models import Thread, Post

from random import randint

# Create your views here.
def index(request):
	# Get all threads
	threads = Thread.objects.all()

	# Get the thread count so pages can be made
	threadcount = threads.count()

	# Get the most recently created 15 threads
	recentthreads = threads.order_by('-pub_date')[:15]

	# Get top 5 comments for each of the last 15 created threads
	replies = [0 for x in range(recentthreads.count())]	
	for i in range(0,threads.count()):
		replies[i] = Post.objects.order_by('-pub_date').filter(thread=recentthreads[i])[:5]
		
	# Generate random numbers for simple captcha
	a = randint(0,10)
	b = randint(0,10)

	d = dict(threads=recentthreads, replies=replies, a=a, b=b, threadcount=threadcount)
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
				date = timezone.now()
				thread = Thread(thread_title=title, thread_text=text, pub_date=date, thread_count=0)
				thread.save()
	
		return HttpResponseRedirect(reverse('index')) 

def reply(request, thread_id):
	p = get_object_or_404(Thread, pk=thread_id)
	try:
		text = request.POST['text']
		if text and len(text) > 5 or len(text) > 2000:
			# Check the captcha length
			a = request.POST['a']
			b = request.POST['b']
			value = request.POST['captcha']
			if int(a) + int(b) == int(value or 0):
				date = timezone.now()
				post = Post(thread=p, post_text=text, pub_date=date)
				post.save()
				p.thread_count += 1
				p.save()
	
		else:
			return render(request, 'board/thread.html', {
                        'thread': p,
                        'error_message': "Bad reply length",
                })

	except (KeyError):		
		return render(request, 'board/thread.html', {
			'thread': p,
			'error_message': "Reply can't be empty",
		})
	else:
		return HttpResponseRedirect(reverse('thread', args=(p.id,)))
