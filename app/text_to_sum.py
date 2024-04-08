import re
from enum import Enum, EnumType
from typing import Type


class TotalSynonyms(Enum):
    SUM = 'Sum'
    GRAND_TOTAL = 'Grand Total'
    TOTAL = 'Total'
    ΣΥΝΟΛΟ = 'ΣΥΝΟΛΟ'


def generate_synonyms_list(enum_class: Type[Enum]) -> list[str]:
    return [syn.value for syn in enum_class]


def extract_list_of_lines_after_total(file_path: str, synonyms: list[str]) -> list[str] | None:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for syn in synonyms:
            for idx, line in enumerate(lines, start=1):
                if syn in line:
                    selected_lines = lines[idx - 1:idx + 7]
                    return selected_lines
    return None


def extract_numbers_from_list_of_totals(list_of_strings: list[str] | None) -> list[float] | None:
    numbers = []
    if list_of_strings is not None:
        for string in list_of_strings:
            numbers.extend([float(num.replace(',', '.')) for num in re.findall(r'-?\d+,\d+', string)])
            numbers.extend([float(num) for num in re.findall(r'-?\d+\.\d+', string)])
        return numbers
    else:
        return None


def get_max_number(numbers: list[float] | None) -> float | None:
    if numbers is not None:
        return max(numbers)
    else:
        return None
