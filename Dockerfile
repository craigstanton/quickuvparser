FROM python:3.7.3-alpine

ADD UVAPIConversion.py /uv/
ADD requirements.txt /uv/
ADD sites.csv /uv/
WORKDIR /uv
RUN pip install -r requirements.txt
