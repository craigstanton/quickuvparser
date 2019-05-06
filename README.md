
Requirements:
=============

* [docker](https://docs.docker.com/install/)

```bash
$ git clone https://github.com/craigstanton/quickuvparser.git
$ cd quickuvparser
$ set the four parameters at the top of the file baseurl, towns, apikey, product
$ docker build -t uv .
$ docker run -v uv python UVAPIConversion.py
```
