# Just an example if postgis support is required
FROM postgres:9.5.4
MAINTAINER Nicola Jordan <nicola.hsr@gmail.com>

RUN apt-get update && apt-get install -y \
    postgresql-9.5-postgis-2.2 \
    postgis \
    && rm -rf /var/lib/apt/lists/*

ADD db/000_create_extensions.sql /docker-entrypoint-initdb.d/000_create_extensions.sql
