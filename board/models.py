from django.db import models
from django.utils import timezone
from django import forms

import datetime

# Create your models here.
class Thread(models.Model):
	thread_title = models.CharField(max_length=50, default=' ')
	thread_text = models.CharField(max_length=2000)
	# auto_now_add=True will set the date automatically when thread is created 
	pub_date = models.DateTimeField(auto_now=False, auto_now_add=True)
	thread_count = models.IntegerField(default=0)
	# auto_now=True will update this last_bumped field each time the thread object is saved
	# which is also whenenver a reply is made to the thread i.e. bumped
	last_bumped = models.DateTimeField(auto_now=True, auto_now_add=True)
	
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published in the last day?'
		

class Post(models.Model):
	thread = models.ForeignKey(Thread)
	post_text = models.CharField(max_length=2000)
	pub_date = models.DateTimeField(auto_now=False, auto_now_add=True)
