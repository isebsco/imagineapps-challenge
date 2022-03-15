FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /ia-challenge
WORKDIR /ia-challenge
ADD . /ia-challenge/
COPY requirements.txt /ia-challenge/
RUN python -m pip install -r requirements.txt
EXPOSE 8080
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 8000
