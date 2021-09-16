
# Yardb

![license](https://img.shields.io/static/v1?label=license&message=MIT&color=informational&style=for-the-badge)
![version](https://img.shields.io/static/v1?label=version&message=0.0.1&color=informational&style=for-the-badge)
![issues](https://img.shields.io/github/issues/jose-gilberto/yardb?style=for-the-badge)

## About

Yardb is a file management system based on a dbms architecture to perform its operations. It uses sql language but contains support for other data types. The project was created for study purposes and should not be used in production. Its future additions should support .tar files and native time series operations.

## Installation (Not Working Yet)

You can install the yardb with pip:

```bash
$ pip install yardb
```

or using the direct github link:
```bash
$ pip install git+https://github.com/jose-gilberto/yardb
```

## Status

The project is now under development.

## Features (v0.0.2)

- Information Catalog
- Information Schema Columns
- Basic DDL statements (```CREATE, ALTER, DROP```)
- Basic DQL statement (```SELECT * FROM ...```)

## How to run
Start the dbms server:
```bash
$ yardb start
```
Open the cli interface for statements:
```bash
$ yardb cli
```

## Requisites

- Python 3

## Contributing

## Contributors

- [José Gilberto](https://github.com/jose-gilberto) - Author