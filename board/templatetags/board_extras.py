from django import template
from django.utils.safestring import mark_safe
from django.utils.html import escape

from board.models import Post, Thread

import re

register = template.Library()

@register.filter
def get_range(value):
	return range(value)

@register.filter(needs_autoescape=True)
def post_urlize(value, autoescape=None):
	value = escape(value)
	return mark_safe(re.sub(r'&gt;&gt;(\d+)', lambda x:  make_links(x.group()), value))

def make_links(value):
	# Get post number and check it's a valid post
	post_number = value[8:]
	if post_number and post_number.isdigit():
		post_number = int(post_number)
		post = Post.objects.filter(id=post_number)
		# Get the thread id so that links can be made across threads
		thread = Thread.objects.filter(post__id=post_number)
		if post:	
			value = '<a href="/thread/' + str(thread[0].id) + '/#' + str(post_number) + '">>>' + str(post_number) + '</a>' 
			return mark_safe(value)


	return escape(value)
