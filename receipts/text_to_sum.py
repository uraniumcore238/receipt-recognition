import re
from pathlib import Path


SYMBOLS_AFTER_TOTAL = 60
decimal_pattern = re.compile(r"-?\d+(?:,\d+|\.\d+)")

synonyms_file = Path('data') / 'total_synonyms.txt'
synonyms = synonyms_file.read_text(encoding="utf-8").splitlines()


def read_receipt(file_path: str) -> str:
    return Path(file_path).read_text(encoding="utf-8")


def extract_total_lines(file_str: str) -> list[str] | None:
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
