
FROM ruby:2.6.2-alpine
LABEL maintainer 'Thorsten Horstmann <mail@thdot.de>'

ENV VERSION 0.5.0

RUN apk add --no-cache --update --virtual=build-dependencies build-base linux-headers gcc g++ \
    && gem install cassandra-web -v ${VERSION} \
    && apk del build-dependencies \
    && rm -rf /tmp/* /var/tmp/* /var/cache/apk/*

CMD ["/bin/sh", "-xc", "exec cassandra-web --hosts ${CASSANDRA_HOST_IPS-127.0.0.1} --port ${CASSANDRA_PORT-9042} --username ${CASSANDRA_USERNAME-cassandra} --password ${CASSANDRA_PASSWORD-cassandra} --bind ${CASSANDRA_WEB_BIND-0.0.0.0:3000}" ]
