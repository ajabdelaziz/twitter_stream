FROM python:3.6
ENV PYTHONUNBUFFERED 1
WORKDIR /twitter
COPY requirements.txt /twitter/
RUN pip install -r requirements.txt
COPY . /code/
