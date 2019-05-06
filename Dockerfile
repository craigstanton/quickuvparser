FROM python:2.7-alpine

ADD UVAPIConversion.py /uv/
ADD requirements.txt /uv/
WORKDIR /uv
RUN pip install -r requirements.txt
