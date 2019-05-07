FROM python:3.7.3-alpine

ADD UVAPIConversion.py /uv/
ADD requirements.txt /uv/
WORKDIR /uv
RUN pip install -r requirements.txt
