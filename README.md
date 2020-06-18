# ComparteRide
A Django-based API Rest application to share rides.

## Suggestions
Work on an UNIX-based OS (MacOS or Linux)

## Requirements
- Docker
- Docker-Compose

## Deployment

### Development
- Build images
`docker-compose -f docker-compose.dev.yml build`

- Run containers
`docker-compose -f docker-compose.dev.yml up -d`

- See containers logs
`docker-compose -f docker-compose.dev.yml logs -f`

- Creating a superuser
`docker-compose -f docker-compose.dev.yml run --rm django python manage.py createsuperuser`

### Test

### Production