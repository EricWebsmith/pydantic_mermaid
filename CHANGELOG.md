# Changelog

This file documents all notable changes to this project.

## [0.5.3] - 2023-12-10

### Changed
- Add CLI parameter check.
- Restore class by order in a list instead of using dict keys.
- Push test case coverage to 100%.
- Use `ruff` to lint project.
- Refactor charts comparing in unit test.

## [0.5.1] - 2023-11-26

### Changed
- Refactor pydantic_parser
- Downgrade pydantic to 1.9

## [0.5.0] - 2023-11-26

### Changed
- Synchonize code from pydantic-2-mermaid (except pydantic parser)
- Exact pydantic parser.
- Support inheritance in command line.
- Bump version from 0.3 to 0.5 directly to keep sync with `pydantic-2-mermaid`

## [0.3.0] - 2023-07-30

### Changed
- Split into two projects, supporting pydantic 1 and 2.
- `generate_chart` now only accepts name parameters.

## [0.2.0] - 2023-03-20

### Added
- Command-line interface for improved usability.
- Inheritance handling: classes now hide properties inherited from parent classes.

### Changed
- Modified the codebase to support Python 3.7, increasing compatibility with older Python versions.

## [0.1.0] - 2023-03-18

### Added
- Initial release of the project, featuring core functionality for generating Mermaid charts from Pydantic models.
