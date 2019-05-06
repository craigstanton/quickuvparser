
Requirements:
=============

* [docker](https://docs.docker.com/install/)

```bash
$ git clone https://github.com/craigstanton/quickuvparser.git
$ cd quickuvparser
set the four parameters at the top of UVAPIConversion.py to match your environment: baseurl, towns, apikey, product
$ docker build -t uv .
$ docker run -v $(pwd)/out:/out uv python UVAPIConversion.py
the output will be in out/uvi-metservice.csv
```
