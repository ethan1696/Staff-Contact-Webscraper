# webscrapper_api
This is the backend for AI Webscrapper

# System Requirements
- Docker
- Python 3.10
- virtualenv package

# Setup
1. Clone the repository
2. Go to project root directory.
3. Run: `cp .env.example .env.local`
4. Build the image using command:
`docker-compose build`
5. To run the container:
`docker-compose up -d` This will run all the required containers in daemon mode. You should be able to see the site running at: http://localhost:8000/api
6. To run migrations:
`docker-compose exec web python manage.py flush --no-input`
`docker-compose exec web python manage.py migrate`
7. To collect static files:
`docker-compose exec web python manage.py collectstatic --no-input --clear`
8. To stop running container
`docker-compose down`

# Reference
https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
