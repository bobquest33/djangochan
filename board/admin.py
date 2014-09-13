from django.contrib import admin
from board.models import Thread
from board.models import Post

class PostInline(admin.TabularInline):
	readonly_fields = ['selflink',]
	model = Post

class ThreadAdmin(admin.ModelAdmin):
	list_display = ('id', 'thread_title', 'thread_text', 'thread_count', 'last_bumped', 'pub_date', 'was_published_recently')
	search_fields = ['thread_title', 'thread_text']
	inlines = [
		PostInline,
	]

class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'post_text', 'pub_date')
	search_fields = ['post_text']


admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post, PostAdmin)
