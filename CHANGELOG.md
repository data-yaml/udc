# CHANGELOG.md

## 0.2.3

- BUG: support BenchlingEntry fields properly
- REFACTOR: use attrs (vs URI) to create resources

## 0.2.2

- REFACTOR: move tools contents under udc

## 0.2.1

- version number in `--version` output
- version-locked quiltplus dependency to avoid breaking changes

## 0.2.0

- add plugins via the `tools` folder
- `udc list` now supports `benchling+https` URIs
- Quilt+ API refactored into its own `quiltplus` package

## 0.1.0

- `cli.yaml` description of arguments and options, inspired by [OpenAPI](https://swagger.io/docs/specification/data-models/data-types/)
- parse Quilt+ URIs (adapted from quiltplus)
- preliminary `udc list` implementation
