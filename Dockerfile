FROM python:3.8-slim
  
RUN pip install -U pip
RUN pip install elasticsearch
RUN pip install flask

RUN mkdir -p /home/flaskr/static

COPY ./app/ /home/
WORKDIR /home/flaskr
CMD ["python", "-u", "app.py"]