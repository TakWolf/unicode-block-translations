from pathlib import Path

PROJECT_ROOT_DIR = Path(__file__).parents[1]
ASSETS_DIR = PROJECT_ROOT_DIR.joinpath('assets')
SRC_DIR = PROJECT_ROOT_DIR.joinpath('src', 'unicode_block_translations')
TRANSLATIONS_DIR = SRC_DIR.joinpath('translations')
TRANSLATIONS_TMP_DIR = PROJECT_ROOT_DIR.joinpath('build', 'translations')
