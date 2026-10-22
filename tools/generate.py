import re
import shutil

import langcodes

from tools import ASSETS_DIR, SRC_DIR, TRANSLATIONS_DIR, TRANSLATIONS_TMP_DIR


def _parse_blocks() -> tuple[str, list[str]]:
    lines = ASSETS_DIR.joinpath('Blocks.txt').read_text('utf-8').splitlines()

    unicode_version = lines[0].removeprefix('# Blocks-').removesuffix('.txt')

    block_names = []
    regex = re.compile(r'\.\.|;\s')
    for line in lines:
        line = line.strip()
        if line == '' or line.startswith('#'):
            continue

        block_name = regex.split(line)[2]
        block_names.append(block_name)

    return unicode_version, block_names


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


def main() -> None:
    unicode_version, block_names = _parse_blocks()

    supported_languages = []

    if TRANSLATIONS_TMP_DIR.exists():
        shutil.rmtree(TRANSLATIONS_TMP_DIR)
    TRANSLATIONS_TMP_DIR.mkdir(parents=True)

    for file_path in TRANSLATIONS_DIR.glob('*.txt'):
        if not file_path.is_file():
            continue

        language = langcodes.standardize_tag(file_path.stem)
        if language == 'en':
            translation = {block_name: block_name for block_name in block_names}
        else:
            translation = _parse_translation(file_path.read_text('utf-8'))

        with TRANSLATIONS_TMP_DIR.joinpath(f'{language}.txt').open('w', encoding='utf-8', newline='\n') as file:
            file.write(f'# Unicode: {unicode_version}\n')
            file.write(f'# {language}\n\n')
            for block_name in block_names:
                localized_name = translation.get(block_name, None)
                if localized_name is None:
                    file.write(f'# TODO # {block_name}:\n')
                else:
                    file.write(f'{block_name}: {localized_name}\n')

        supported_languages.append(language)

    if TRANSLATIONS_DIR.exists():
        shutil.rmtree(TRANSLATIONS_DIR)
    TRANSLATIONS_TMP_DIR.rename(TRANSLATIONS_DIR)

    meta_lines = []
    meta_lines.append('from typing import Final')
    meta_lines.append('')
    meta_lines.append(f'UNICODE_VERSION: Final = {unicode_version!r}')
    meta_lines.append('')
    meta_lines.append('SUPPORTED_LANGUAGES: Final = (')
    for language in sorted(supported_languages):
        meta_lines.append(f'    {language!r},')
    meta_lines.append(')')
    meta_lines.append('')

    SRC_DIR.mkdir(parents=True, exist_ok=True)
    SRC_DIR.joinpath('meta.py').write_text('\n'.join(meta_lines), 'utf-8')


if __name__ == '__main__':
    main()
