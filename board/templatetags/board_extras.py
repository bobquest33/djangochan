from django import template
from django.utils.safestring import mark_safe

import re

register = template.Library()

@register.filter
def get_range(value):
	return range(value)

@register.filter(is_safe=True, needs_autoescape=True)
def post_urlize(value, autoescape=None):
	# Use regex to find all post links and make them linkable
	return mark_safe(re.sub(r'>>(\d+)\b', r'<a href="#\1">>>\1</a>', value))
