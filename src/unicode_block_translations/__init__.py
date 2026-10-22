from importlib import resources

import langcodes

from unicode_block_translations.meta import UNICODE_VERSION, SUPPORTED_LANGUAGES

_TRANSLATIONS_DIR = resources.files(__package__).joinpath('translations')

_translations = {}


def _parse_translation(text: str) -> dict[str, str]:
    translation = {}
    for line in text.splitlines():
        line = line.strip()
        if line == '' or line.startswith('#'):
            continue

        parts = line.split(':', 1)
        if len(parts) == 2:
            translation[parts[0].strip()] = parts[1].strip()
    return translation


def translate(
        block_name: str,
        language: str,
        default: str | None = None,
) -> str | None:
    closest_language = langcodes.closest_supported_match(language, SUPPORTED_LANGUAGES)

    if closest_language is None:
        return default

    if closest_language in _translations:
        translation = _translations[closest_language]
    else:
        translation = _parse_translation(_TRANSLATIONS_DIR.joinpath(f'{closest_language}.txt').read_text('utf-8'))
        _translations[closest_language] = translation
    return translation.get(block_name, default)
