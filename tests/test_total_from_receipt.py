import datetime

from receipts.text_to_sum import extract_totals, get_max_number, extract_total_lines, total_synonyms
from unittest.mock import patch


def test__total_from_receipt__return_total_sum_of_the_receipt():
    with patch('receipts.text_to_sum.extract_total_lines') as extract_total_lines_mock:
        extract_total_lines_mock.return_value = ['0,00\n2,27\n2,27\nTotal\n1,63\n34,77\n36,40\n0124 692544/03\n15.02.24 18:55']
        list_of_numbers = extract_totals(extract_total_lines_mock.return_value)
        max_sum = get_max_number(list_of_numbers)
        assert max_sum == 36.4


def test__extract_total_lines__return_list_of_nums_after_total():
    assert extract_total_lines('0,00\n2,27\n2,27\nTotal\n1,63\n34,77\n36,40\n0124 692544/03\n15.02.24 18:55', total_synonyms) == ['Total\n1,63\n34,77\n36,40\n0124 692544/03\n15.02.24 18:55']


def test__extract_total_lines__return_none_if_total_not_found(make_receipt):
    receipt = make_receipt(total_part="unknown")
    assert extract_total_lines(receipt, synonyms=["TOTAL", "total"]) is None


def test__extract_total_lines__return_lines_below_total_if_total_found(make_receipt):
    receipt = make_receipt(total_part="total: 150.22")
    today = datetime.date.today()
    assert extract_total_lines(receipt, synonyms=["TOTAL", "total"]) == [f'total: 150.22\n{today}']


def test__extract_totals__return_float_from_all_numbers():
    any_numbers_in_receipt = ['15.22', '150,5', '147', '0007895', '13:25']
    assert extract_totals(any_numbers_in_receipt) == [15.22, 150.5]


def test__extract_totals__return_empty_list_from_all_numbers_if_float_not_found():
    any_numbers_in_receipt = ['147', '0007895', '13:25']
    assert extract_totals(any_numbers_in_receipt) == []
