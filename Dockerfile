FROM python:3.7-slim

# Place your flask application on the server
COPY ./flask /flask
WORKDIR /flask

RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential
	
RUN pip3 install --no-cache-dir -r requirements.txt

COPY nginx.conf /etc/nginx
RUN chmod +x ./start.sh
CMD ["./start.sh"]