FROM alpine:latest

RUN apk add --no-cache curl

COPY config.txt /app/config.txt

VOLUME /data

CMD ["echo", "Hello, Docker Volumes!"]