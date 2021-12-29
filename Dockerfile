FROM python:3.8.3
# set work directory
WORKDIR /usr/src/forecast_api
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r /usr/src/requirements.txt
# copy project
COPY . /usr/src/forecast_api

EXPOSE 8000
CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]
