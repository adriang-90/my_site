# pull oficial base image
FROM python:3.8.5


# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1


# set work directory
WORKDIR /my_site


# Install dependencies
COPY Pipfile Pipfile.lock /my_site/
RUN pip install pipenv && pipenv install --system


# Copy project
COPY . /my_site/


