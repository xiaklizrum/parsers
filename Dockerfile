FROM python:latest
WORKDIR /tmp
ENV PYTHONPATH=/tmp 
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install --requirement /tmp/requirements.txt