import pytest

import unicode_block_translations


def test_unicode_version() -> None:
    assert unicode_block_translations.UNICODE_VERSION == '18.0.0'


@pytest.mark.parametrize(
    ('block_name', 'zh_cn_name', 'zh_hk_name', 'zh_tw_name'),
    [
        ('Basic Latin', '基本拉丁字母', '基本拉丁字母', '基本拉丁字母'),
        ('Lao', '老挝文', '老撾文', '寮文'),
        ('Georgian', '格鲁吉亚字母', '格魯吉亞字母', '喬治亞字母'),
        ('Optical Character Recognition', '光学字符识别', '光學字符辨識', '光學字元辨識'),
        ('High Surrogates', '高位代理项', '高代理區', '高代理區'),
        ('Playing Cards', '纸牌', '紙牌', '紙牌'),
        ('Cyrillic Extended-A', '西里尔字母扩充-A', '西里爾字母擴充-A', '西里爾字母擴充-A'),
        ('Arabic Extended-A', '阿拉伯文扩充-A', '阿拉伯文擴充-A', '阿拉伯文擴充-A'),
        ('Myanmar Extended-A', '缅甸文扩充-A', '緬甸文擴充-A', '緬甸文擴充-A'),
        ('Tangut Components', '西夏文构件', '西夏文構件', '西夏文構件'),
        ('Linear A', '线形文字 A', '線形文字 A', '線形文字 A'),
    ],
)
def test_translate(block_name: str, zh_cn_name: str, zh_hk_name: str, zh_tw_name: str) -> None:
    assert unicode_block_translations.translate(block_name, 'en') == block_name
    assert unicode_block_translations.translate(block_name, 'zh') == zh_cn_name
    assert unicode_block_translations.translate(block_name, 'zh-cn') == zh_cn_name
    assert unicode_block_translations.translate(block_name, 'zh-hk') == zh_hk_name
    assert unicode_block_translations.translate(block_name, 'zh-tw') == zh_tw_name


def test_no_translation() -> None:
    assert unicode_block_translations.translate('Not A Block Name', 'en') is None
    assert unicode_block_translations.translate('Not A Block Name', 'en', 'Default Block Name') == 'Default Block Name'

    assert unicode_block_translations.translate('Basic Latin', 'no-language') is None
    assert unicode_block_translations.translate('Basic Latin', 'no-language', 'Default Block Name') == 'Default Block Name'
