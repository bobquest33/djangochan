from django.core.management.base import BaseCommand
from board.models import Thread

class Command(BaseCommand):
	help = 'Deletes oldest threads over the 225 thread limit (15 threads per page, 15 pages = 225)'
	
	def handle(self, *args, **options):
		# Check if any threads need deleting first
		all_threads_count = Thread.objects.all().count()
		if all_threads_count > 225:
			# Delete all the threads which will delete posts in it as well
			threads = Thread.objects.order_by('last_bumped')[225:].values_list("id", flat=True)
			Thread.objects.filter(pk__in=list(threads)).delete()
