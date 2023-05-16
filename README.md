# UDC

## The Universal Data Client

### What is UDC?

Universal Data is an open source initiative to build a decentralized, cryptographically-secure ecosystem containerizing both structured and unstructured data.  UDC is the first client for that system.

## Installation

When installing from GitHub:

```bash
poetry install
```

```bash
poetry run udc
```

<!--pytest-codeblocks:expected-output-->
```bash
Usage: udc [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  list  Simple program that lists contents URI.
```

## Usage

### List contents of individual packages

```bash
poetry run udc list "quilt+s3://quilt-example#package=examples/wellplates:latest"
```

### List all versions of a package

```bash
poetry run udc list "quilt+s3://quilt-example#package=examples/wellplates"
```

### List all packages in a registry

```bash
poetry run udc list quilt+s3://quilt-example
```
