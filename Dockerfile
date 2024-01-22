FROM python:3.12

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt-get update && apt-get -y install netcat-traditional &&  apt-get -y install gettext &&  apt-get -y install nano && apt-get -y install wkhtmltopdf

RUN mkdir /email_tracker

# Install dependencies
COPY /requirements /email_tracker/requirements
RUN pip install -r /email_tracker/requirements/dev.txt

WORKDIR /email_tracker
COPY . /email_tracker

RUN ["chmod", "+x", "/email_tracker/entrypoint.sh"]