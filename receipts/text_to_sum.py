import re

total_synonyms = ['Sum', 'Grand Total', 'Total', 'ΣΥΝΟΛΟ']


def read_file(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        text = ''.join(lines)
        return text


def extract_total_lines(file_str: str, synonyms: list[str]) -> list[str] | None:
    for syn in synonyms:
        start_index = file_str.find(syn)
        end_index = file_str.find(syn)+60
        if syn in file_str:
            extracted_text = [file_str[start_index:end_index]]
            return extracted_text
    return None


def extract_totals(total_lines: list[str] | None) -> list[float] | None:
    numbers = []
    decimal_pattern = re.compile(r'-?\d+(?:,\d+|\.\d+)')
    if total_lines is not None:
        for line in total_lines:
            numbers.extend([float(num.replace(',', '.')) for num in decimal_pattern.findall(line)])
        return numbers
    return None


def get_max_number(numbers: list[float] | None) -> float | None:
    if numbers is not None:
        return max(numbers)
    return None
