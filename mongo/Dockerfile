FROM mongo:latest
COPY /initdb/init-mongo.js /docker-entrypoint-initdb.d/
RUN chmod a+r /docker-entrypoint-initdb.d/*

# USER surya