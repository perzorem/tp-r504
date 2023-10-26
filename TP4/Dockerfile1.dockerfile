FROM debian:11
RUN apt-get update $$ apt-get upgrade -y
RUN apt-get install -y build-essential pkg-config python-dev python3-pip default-libmysqlclient-dev
RUN pip3 install --upgrade pip
RUN pip3 install flask-mysqldb mysql-connector-python
RUN mkdir -p /srv/templates
RUN copy index.html /srv/templates
RUN copy app1.py /srv/
CMD["flask","--app","/srv/app1","run","--host=0.0.0.0"]