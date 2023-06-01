# UDC

## The Universal Data Client

### What is UDC?

Universal Data is an open source initiative to build
a decentralized, cryptographically-secure ecosystem
containerizing both structured and unstructured data.

UDC is the initial (alpha) client for that system.
It currently supports both Quilt and Benchling URIs.
For example:

- `udc list "quilt+s3://quilt-example#package=examples/wellplates"`
- `udc patch "benchling+https://dtt.benchling.com?name=Update#type=Entry&id=etr_123"`

## Installation

### Production Package

From PyPi:

<!--pytest.mark.skip-->
```bash
python3 -m pip install udc # OR
python3 -m pip install --upgrade udc
which udc
```

## Development Branch

<!--pytest.mark.skip-->
```bash
python3 -m pip install https://github.com/data-yaml/udc@main
```

## Cloned

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
udc # prints help
```

### List contents of a specific package instance

```bash
udc list "quilt+s3://quilt-example#package=examples/wellplates@6782cf98a2"
```

e.g.,
<!--pytest-codeblocks:expected-output-->
```bash
"quilt+s3://quilt-example#package=examples/wellplates@6782cf98a2&path=README.md"
"quilt+s3://quilt-example#package=examples/wellplates@6782cf98a2&path=autoplate_H1N1.csv"
"quilt+s3://quilt-example#package=examples/wellplates@6782cf98a2&path=data_products.ipynb"
"quilt+s3://quilt-example#package=examples/wellplates@6782cf98a2&path=neutralisation-altair.json"
"quilt+s3://quilt-example#package=examples/wellplates@6782cf98a2&path=neutralisation.json"
"quilt+s3://quilt-example#package=examples/wellplates@6782cf98a2&path=quilt_summarize.json"
"quilt+s3://quilt-example#package=examples/wellplates@6782cf98a2&path=render.html"
```

### List all versions of a package

```bash
udc list "quilt+s3://quilt-example#package=examples/wellplates" | head -n 1
```

e.g.,
<!--pytest-codeblocks:expected-output-->
```bash
"quilt+s3://quilt-example#package=examples/wellplates@6782cf98a2c600f4c519efd5de868d5ef1e05ac92fcb0fa56044bb8c925c5f02"
```

### List all packages in a registry

```bash
udc list quilt+s3://quilt-example | head -n 1
```

e.g.,
<!--pytest-codeblocks:expected-output-->
```bash
"quilt+s3://quilt-example#package=akarve/amazon-reviews:latest"
```

## Development

### Testing

<!--pytest.mark.skip-->
```bash
make test
```

### Continuous Monitoring

<!--pytest.mark.skip-->
```bash
make watch
```

### Create Package

WARNING: Do this only if you are the maintainer of the package.

Be sure you to first set your [~/.pypirc](https://pypi.org/manage/account/) using `poetry config pypi-token.pypi <pypi-api-token>`

<!--pytest.mark.skip-->
```bash
# merge PR
make tag
make pypi
poetry publish
```
