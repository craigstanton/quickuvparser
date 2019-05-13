
Requirements:
=============

* [docker](https://docs.docker.com/install/)

```bash
$ git clone https://github.com/craigstanton/quickuvparser.git
$ cd quickuvparser
```

Usage:
======

*Docker*
```
$ docker build -t uv .
$ docker run -v $(pwd)/out:/out uv python UVAPIConversion.py [OPTIONS]
```
the output will be in out/uvi-forecasts.csv


*CLI*
```bash
$ python UVAPIConversion.py [OPTIONS]
```

```
Options:
  --baseurl TEXT  API base URL
  --apikey TEXT   API key  [required]
  --product TEXT  Product. 1 = cloudy sky, 0 = clear sky
  --help          Show this message and exit.
```