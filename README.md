djangochan
==========

4chan-like Image Board using Django


###My Setup

I use nginx to forward connections to gunicorn as well as serve the static files. I monitor gunicorn with supervisord. Using postgresql for the database 

####To Be Done
  - Posts with images
  - Catalog view
  - Ability for admins to create new boards
  - Add sticky posts 
  - Dynamically resize images to create thumbnails (current just forced size in the html)
  - Thumbnails should link to original image

###Implemented
  - Threads can have an image
  - Post linking
  - Post creation
  - Thread creation
  - Thread bumping with a limit of 300 posts
  - Multiple pages to show all threads
  - Admin backend to manage threads and posts
  - Thread pruning can be done by running a cron job to execute 'python manage.py prunethreads'
