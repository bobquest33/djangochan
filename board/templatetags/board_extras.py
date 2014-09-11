from django import template
from django.utils.safestring import mark_safe
from django.utils.html import conditional_escape

import re

register = template.Library()

@register.filter
def get_range(value):
	return range(value)

@register.filter(needs_autoescape=True)
def post_urlize(value, autoescape=None):
	# Use regex to find all post links and make them linkable
	return mark_safe(re.sub(r'&gt;&gt;(\d+)\b', r'<a href="#\1">>>\1</a>', value))
