import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
# позитивные сценарии:

# 1. ПРИМЕР

# @pytest.mark.parametrize("input_str, expected", [
#     ("skypro", "Skypro"),
#     ("hello world", "Hello world"),
#     ("python", "Python"),
# ])
# def test_capitalize_positive(input_str, expected):
#     assert string_utils.capitalize(input_str) == expected

# 2. Принимает на вход текст и удаляет пробелы в начале, если они есть

@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("   123", "123"),
    ("   04 апреля 2023", "04 апреля 2023")
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

# 3. Возвращает `True`, если строка содержит искомый символ и `False` - если нет

@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "S", True), ("SkyPro", "U", False),
    ("1234", "3", True), ("1234", "5", False),
    ("Elena G", "Elena G", True), ("Elena G", "Elena L", False)
])
def test_contains_positive(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

# 4. Удаляет все подстроки из переданной строки

@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro", "k", "SyPro"), ("SkyPro", "Pro", "Sky"),
    ("SkyPro125", "1", "SkyPro25"), ("SkyPro125", "Pro125", "Sky"),
    ("SkyPro school", "o", "SkyPr schl"), ("SkyPro school", "school", "SkyPro ")
])
def test_delete_symbol_positive(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected

@pytest.mark.negative

# 1. ПРИМЕР
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# 2. Принимает на вход текст и удаляет пробелы в начале, если они есть

@pytest.mark.parametrize("input_str, expected", [
    ("   ", ""),
    ("   $%^-+", "$%^-+")
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# 3. Возвращает `True`, если строка содержит искомый символ и `False` - если нет

@pytest.mark.parametrize("string, symbol, expected", [
    ("", "", True), ("5", "6", False),
    ("    ", "    ", True), ("%$#", "&*^", False)
])
def test_contains_negative(string, symbol, expected):
    assert string_utils.contains(string, symbol) == expected

# 4. Удаляет все подстроки из переданной строки

@pytest.mark.parametrize("string, symbol, expected", [
    ("SkyPro $%^", "k", "SyPro $%^"), ("", "", "")
])
def test_delete_symbol_negative(string, symbol, expected):
    assert string_utils.delete_symbol(string, symbol) == expected