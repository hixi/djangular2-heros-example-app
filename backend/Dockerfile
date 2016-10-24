FROM python:3.5

RUN apt-get update && apt-get install -y python3-psycopg2

ENV USER py

ADD ./wait-for-it/wait-for-it.sh /bin/wait-for-it.sh
ADD ./requirements.txt /var/data/backend/requirements.txt
RUN pip3 install -r /var/data/backend/requirements.txt

ADD . /backend
COPY ./docker-entrypoint.sh /bin/docker-entrypoint.sh

ENV PORT=8000
EXPOSE ${PORT}
WORKDIR /backend/heroes_example
ENTRYPOINT ["/bin/docker-entrypoint.sh"]

CMD /usr/local/bin/gunicorn heroes_example.wsgi:application --bind 0.0.0.0:${PORT}
