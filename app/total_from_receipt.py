from app.text_to_sum import generate_synonyms_list, extract_list_of_lines_after_total, TotalSynonyms, extract_numbers_from_list_of_totals, \
    get_max_number


def total_from_receipt(file_path: str) -> float | None:
    synonyms_list = generate_synonyms_list(TotalSynonyms)
    list_of_strings_under_total = extract_list_of_lines_after_total(file_path, synonyms_list)
    list_of_numbers = extract_numbers_from_list_of_totals(list_of_strings_under_total)
    max_sum = get_max_number(list_of_numbers)
    if max_sum is not None:
        return max_sum
    else:
        return None





print(total_from_receipt(r'C:\Users\urani\Documents\Programming\Python_projects\receipt-recognition\texts\receipt_one.txt'))
print(total_from_receipt(r'C:\Users\urani\Documents\Programming\Python_projects\receipt-recognition\texts\receipt_two.txt'))
print(total_from_receipt(r'C:\Users\urani\Documents\Programming\Python_projects\receipt-recognition\texts\receipt_three.txt'))