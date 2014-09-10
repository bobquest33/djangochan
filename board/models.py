from django.db import models
from django.utils import timezone
from django import forms

import datetime

# Create your models here.
class Thread(models.Model):
	thread_title = models.CharField(max_length=50, default=' ')
	thread_text = models.CharField(max_length=2000)
	pub_date = models.DateTimeField('date published')
	thread_count = models.IntegerField(default=0)

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published in the last day?'

class Post(models.Model):
	thread = models.ForeignKey(Thread)
	post_text = models.CharField(max_length=2000)
	pub_date = models.DateTimeField('date published')
