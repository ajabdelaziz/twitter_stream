FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir /twitter
WORKDIR /twitter
COPY requirements.txt /twitter/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD exec gunicorn twitter.wsgi:application --bind 0.0.0.0:8000 --workers 3
