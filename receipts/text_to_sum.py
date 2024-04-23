import re
from pathlib import Path
import tests

SYMBOLS_AFTER_TOTAL = 60
decimal_pattern = re.compile(r"-?\d+(?:,\d+|\.\d+)")


def read_file_data(file_path: Path) -> list[str]:
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()


def read_receipt(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        return ''.join(lines)


def extract_total_lines(file_str: str) -> list[str] | None:
    synonyms = read_file_data(Path(tests.__file__).parent.parent.joinpath('data/total_synonyms.txt'))
    for syn in synonyms:
        syn_no_spaces = syn.strip()
        if syn_no_spaces in file_str:
            start_index = file_str.find(syn_no_spaces)
            end_index = start_index + SYMBOLS_AFTER_TOTAL
            return [file_str[start_index:end_index]]
    return None


def potential_totals(line: str) -> list[float]:
    numbers = []
    decimal_p = decimal_pattern
    numbers.extend([float(num.replace(",", ".")) for num in decimal_p.findall(line)])
    return numbers


def extract_totals(total_lines: list[str]) -> list[float]:
    numbers = []
    if total_lines:
        for line in total_lines:
            numbers.extend(potential_totals(line))
        return numbers
    return []
