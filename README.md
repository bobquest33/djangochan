djangochan
==========

4chan-like Image Board using Django


###My Setup

I use nginx to forward connections to gunicorn as well as serve the static files. I monitor gunicorn with supervisord. Using postgresql for the database 

####To Be Done

  - Thread bumping
  - Post linking
  - Improve admin backend so that posts have a link to their thread and threads display posts
  - Redesign entire css/html of the board
  - Images?
