# CHANGELOG.md

## 0.3.3 (2023-06-08)

- Bump version to fix packaging issues

## 0.3.2 (2023-06-02)

- New quiltplus version
- verify get/put/patch

## 0.3.1 (2023-05-31b)

- Support BenchlingEntry get/patch
- Make `dir` an option versus a positional argument
- New `ResultList` output type

## 0.3.0 (2023-05-31)

- Extract UnYaml to its own package
- Ensure GitHub Actions testing Bechling (to improve coverage)
- Fix type-hint errors

## 0.2.5 (2023-05-29)

- Peg to Python 3.10+ so TempDirectory works on Windows
- Work with QuiltPlus 0.9
- Require anyio v3.7+

## 0.2.4

Patch release to support QuiltPlus 0.9

- Remove QuiltID, QuiltConfig dependency
- Remove QuiltConfig, GitIgnore
- Make QuiltResource forward-compatible

## 0.2.3

- BUG: support BenchlingEntry fields properly
- REFACTOR: use attrs (vs URI) to create resources
- Quote field names with '+' character

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
