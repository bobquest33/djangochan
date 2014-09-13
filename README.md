djangochan
==========

4chan-like Image Board using Django


###My Setup

I use nginx to forward connections to gunicorn as well as serve the static files. I monitor gunicorn with supervisord. Using postgresql for the database 

####To Be Done
  - Redesign entire css/html of the board
  - Images
  - Thread pruning

###Implemented
  - Post creation
  - Thread creation
  - Thread bumping with a limit of 300 posts
  - Multiple pages to show all threads
  - Admin backend to manage threads and posts
