#!/bin/bash
set -e
/bin/wait-for-it.sh -t 30 database:5432
yes "yes" | python ./manage.py migrate
python3 manage.py collectstatic --noinput
exec "$@"
