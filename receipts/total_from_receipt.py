from receipts.text_to_sum import extract_total_lines, total_synonyms, extract_totals, \
    get_max_number, read_file


def total_from_receipt(file_path: str) -> float | None:
    text = read_file(file_path)
    list_of_strings_under_total = extract_total_lines(text, total_synonyms)
    list_of_numbers = extract_totals(list_of_strings_under_total)
    return get_max_number(list_of_numbers)


