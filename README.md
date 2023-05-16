# UDC

## The Universal Data Client

### What is UDC?

Universal Data is an open source initiative to build a decentralized, cryptographically-secure ecosystem containerizing both structured and unstructured data.  UDC is the first client for that system.

## Installation

From PyPi (when published):

<!--pytest-codeblocks:skip-->
```bash
python3 -m pip install --upgrade pip
python3 -m pip install udc
```

When cloned from [GitHub](https://github.com/data-yaml/udc):

```bash
poetry install
```

<--

```bash
alias udc="poetry run udc"
```
-->

## Usage

```bash
udc
```

<!--pytest-codeblocks:expected-output-->
```bash
Usage: udc [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  list  Simple program that lists contents URI.
```

### List contents of individual packages

```bash
udc list "quilt+s3://quilt-example#package=examples/wellplates:latest"
```

### List all versions of a package

```bash
udc list "quilt+s3://quilt-example#package=examples/wellplates"
```

### List all packages in a registry

```bash
udc list quilt+s3://quilt-example
```

## Development

### Testing

<!--pytest-codeblocks:skip-->
```bash
make test
```

### Continuous Monitoring

<!--pytest-codeblocks:skip-->
```bash
make watch
```

### Code Coverage

<!--pytest-codeblocks:skip-->
```bash
make coverage
```

### Create Package

<!--pytest-codeblocks:skip-->
```bash
make package
```
