FROM python:3.10

#RUN mkdir "/site"
WORKDIR ./usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
#RUN python manage.py migrate

#CMD ['python', 'manage.py', 'migrate']

COPY . .