# 99minutos_pagination

[![Build Status](https://travis-ci.org/cesarmanzo/99minutos_pagination.svg?branch=master)](https://travis-ci.org/cesarmanzo/99minutos_pagination)
[![Built with](https://img.shields.io/badge/Built_with-Cookiecutter_Django_Rest-F7B633.svg)](https://github.com/agconti/cookiecutter-django-rest)

Ejemplo de paginación para 99minutos. Check out the project's [documentation](http://cesarmanzo.github.io/99minutos_pagination/).

# Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  
- [Travis CLI](http://blog.travis-ci.com/2013-01-14-new-client/)
- [Heroku Toolbelt](https://toolbelt.heroku.com/)

# Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

# Continuous Deployment

Deployment is automated via Travis. When builds pass on the master or qa branch, Travis will deploy that branch to Heroku. Follow these steps to enable this feature.

Initialize the production server:

```
heroku create 99minutos_pagination-prod --remote prod && \
    heroku addons:create newrelic:wayne --app 99minutos_pagination-prod && \
    heroku addons:create heroku-postgresql:hobby-dev --app 99minutos_pagination-prod && \
    heroku config:set DJANGO_SECRET_KEY=`openssl rand -base64 32` \
        DJANGO_AWS_ACCESS_KEY_ID="Add your id" \
        DJANGO_AWS_SECRET_ACCESS_KEY="Add your key" \
        DJANGO_AWS_STORAGE_BUCKET_NAME="99minutos_pagination-prod" \
        DJANGO_CONFIGURATION="Production" \
        DJANGO_SETTINGS_MODULE="99minutos_pagination.config" \
        --app 99minutos_pagination-prod
```

Initialize the qa server:

```
heroku create 99minutos_pagination-qa --remote qa && \
    heroku addons:create newrelic:wayne --app 99minutos_pagination-qa && \
    heroku addons:create heroku-postgresql:hobby-dev --app 99minutos_pagination-qa && \
    heroku config:set DJANGO_SECRET_KEY=`openssl rand -base64 32` \
        DJANGO_AWS_ACCESS_KEY_ID="Add your id" \
        DJANGO_AWS_SECRET_ACCESS_KEY="Add your key" \
        DJANGO_AWS_STORAGE_BUCKET_NAME="99minutos_pagination-qa" \
        DJANGO_CONFIGURATION="Production" \
        DJANGO_SETTINGS_MODULE="99minutos_pagination.config" \
        --app 99minutos_pagination-qa
```

Securely add your Heroku credentials to Travis so that it can automatically deploy your changes:

```bash
travis encrypt HEROKU_AUTH_TOKEN="$(heroku auth:token)" --add
```

Commit your changes and push to master and qa to trigger your first deploys:

```bash
git commit -a -m "ci(travis): add Heroku credentials" && \
git push origin master:qa && \
git push origin master
```

You're now ready to continuously ship! ✨ 💅 🛳
