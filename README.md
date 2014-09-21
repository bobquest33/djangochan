djangochan
==========

4chan-like Image Board using Django


###My Setup

I use nginx to forward connections to gunicorn as well as serve the static files. I monitor gunicorn with supervisord. Using postgresql for the database 

####To Be Done
  - Redesign entire css/html of the board
  - Images
  - Catalog view

###Implemented
  - Post linking
  - Post creation
  - Thread creation
  - Thread bumping with a limit of 300 posts
  - Multiple pages to show all threads
  - Admin backend to manage threads and postsi
  - Thread pruning can be done by running a cron job to execute 'python manage.py prunethreads'
