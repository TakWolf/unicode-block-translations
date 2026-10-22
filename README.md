# Unicode Block Translations

[![Python](https://img.shields.io/badge/python-3.10-brightgreen?style=flat-square)](https://www.python.org)
[![PyPI](https://img.shields.io/pypi/v/unicode-block-translations?style=flat-square)](https://pypi.org/project/unicode-block-translations/)

Translations of Unicode block names, with support for language and regional variants.

## Installation

```shell
pip install unicode-block-translations
```

## Usage

```python
import unicode_block_translations

assert unicode_block_translations.translate('Basic Latin', 'zh') == '基本拉丁字母'
```

## Dependencies

- [Langcodes](https://github.com/rspeer/langcodes)

## License

[MIT License](LICENSE)
