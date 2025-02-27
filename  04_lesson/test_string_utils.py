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

@pytest.mark.parametrize("string, symbol", [
    ("SkyPro", "S"), ("SkyPro", "U"),
    ("1234", "3"), ("1234", "5"),
    ("Elena G", "Elena G"), ("Elena G", "Elena L")
])
def test_contains_positive(string, symbol):
    assert string_utils.contains("SkyPro", "S") == True
    assert string_utils.contains("SkyPro", "U") == False
    return symbol in string

# 4. Удаляет все подстроки из переданной строки

@pytest.mark.parametrize("string, symbol", [
    ("SkyPro", "k"), ("SkyPro", "Pro"),
    ("SkyPro125", "1"), ("SkyPro125", "Pro125"),
    ("SkyPro school", "o"), ("SkyPro school", "school")
])
def test_delete_symbol_positive(string, symbol):
    string = string
    symbol = symbol
    result = string.replace(symbol, "")
    return result


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

@pytest.mark.parametrize("string, symbol", [
    ("", ""), ("5", "6"),
    ("    ", "    "), ("%$#", "&*^")
])
def test_contains_negative(string, symbol):
    assert string_utils.contains("SkyPro", "S") == True
    assert string_utils.contains("SkyPro", "U") == False
    return symbol in string

# 4. Удаляет все подстроки из переданной строки

@pytest.mark.parametrize("string, symbol", [
    ("SkyPro $%^", "k"), ("", "Pro"),
    ("", ""), ("  ", "  ")
])
def test_delete_symbol_negative(string, symbol):
    string = string
    symbol = symbol
    result = string.replace(symbol, "")
    return result
