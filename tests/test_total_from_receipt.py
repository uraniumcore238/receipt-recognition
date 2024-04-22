import datetime
from pathlib import Path
from unittest.mock import patch
from receipts.text_to_sum import extract_totals, extract_total_lines, read_file_data, \
    potential_totals


def test__read_file_data__return_file_value_as_list():
    with patch("receipts.text_to_sum.open") as open_mock:
        open_mock.return_value.__enter__.return_value.readlines.return_value = ["line1\n",
                                                                                "line2\n",
                                                                                "line3\n"]
        file_path = Path("test.txt")
        result = read_file_data(file_path)
        assert result == ["line1\n", "line2\n", "line3\n"]


def test__read_receipt__return_file_value_as_string():
    with patch("receipts.text_to_sum.open") as open_mock:
        open_mock.return_value.__enter__.return_value.readlines.return_value = ("line1\nline2\n"
                                                                                "line3\n")
        file_path = Path("test.txt")
        result = read_file_data(file_path)
        assert result == "line1\nline2\nline3\n"


def test__extract_total_lines__return_list_of_nums_after_total():
    assert (extract_total_lines('0,00\n2,27\n2,27\nTotal\n1,63\n34,77\n36,40\n0124692544/03\n'
                                '15.02.24 18:55') ==
            ['Total\n1,63\n34,77\n36,40\n0124692544/03\n15.02.24 18:55'])


def test__extract_total_lines__return_list_of_nums_after_total_but_no_more_than_limit():
    assert (extract_total_lines('0,00\n2,27\n2,27\nTotal\n1,63\n34,77\n36,40\n0124692544/03\n'
                                '15.02.24 18:55 123456789123456789') ==
            ['Total\n1,63\n34,77\n36,40\n0124692544/03\n15.02.24 18:55 12345678'])


def test__extract_total_lines__return_none_if_total_not_found(make_receipt):
    receipt = make_receipt(total_part="unknown")
    assert extract_total_lines(receipt) is None


def test__extract_total_lines__return_lines_below_total_if_total_found(make_receipt):
    receipt = make_receipt(total_part="total: 150.22")
    today = datetime.date.today()
    assert extract_total_lines(receipt) == [f'total: 150.22\n{today}']


def test__extract_totals__return_only_floats_from_all_numbers():
    any_numbers_in_receipt = ['15.22', '150,5', '147', '0007895', '13:25']
    assert extract_totals(any_numbers_in_receipt) == [15.22, 150.5]


def test__extract_totals__return_empty_list_from_all_numbers_if_float_not_found():
    any_numbers_in_receipt = ['147', '0007895', '13:25']
    assert extract_totals(any_numbers_in_receipt) == []


def test__extract_totals__return_empty_list_from_all_numbers_if_got_empty_list():
    assert extract_totals([]) == []


def test__potential_totals__return_floats_from_the_string():
    assert (potential_totals('0,00\n2,27\n2,27\nTotal\n1,63\n34,77\n36,40\n0124692544/03\n'
                                '15.02.24 18:55 123456789123456789') ==
            [0.0, 2.27, 2.27, 1.63, 34.77, 36.4, 15.02])


def test__potential_totals__return_empty_list_if_got_empty_string():
    assert potential_totals('') == []
