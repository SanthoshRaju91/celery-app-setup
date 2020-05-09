# Celery project setup

Setup instruction

1. Copy the required folders and files to build folder for a smaller build context

   `cp -R src build/`
   `cp -R distrib build/`
   `cp requirements.txt build/`

2. Building the docker container

   `docker build --name celery-server -f distrib/Dockerfile build/`

3. Running the application

   `docker run -d -p 6379:6379 redis`
   `docker run -d -p 5672:5672 rabbitmq`
   `docker run -d --link redis:redis --link rabbitmq:rabbitmq --name celery-server celery-server`

4. Or with docker compose

   `docker-compose up`
