FROM alpine:edge

# install system dependencies
RUN apk add --no-cache \
    py3-pip \
    py3-pillow \
    python3

# install python dependencies
WORKDIR /tmp
COPY requirements.txt .
RUN pip3 install -r requirements.txt \
    && rm requirements.txt \
    && mkdir -p /srv/app

# install app
WORKDIR /srv/app
COPY daas .

# run app
CMD gunicorn -b 0.0.0.0:80 daas.wsgi
