from enum import Enum
from app.text_to_sum import generate_synonyms_list, extract_list_of_lines_after_total, get_max_number


def test__generate_synonyms_list__return_list_of_strings():
    class TestSynonyms(Enum):
        TOTAL = 'Total'
        SUM = 'Sum'
        AMOUNT = 'Amount'
        GRAND_TOTAL = 'Grand Total'

    assert generate_synonyms_list(TestSynonyms) == ['Total', 'Sum', 'Amount', 'Grand Total']


def test__extract_list_of_lines_after_total__(file_path):
    assert (extract_list_of_lines_after_total(file_path, ['Total', 'Sum', 'Amount', 'Grand Total']) ==
            ['Total\n', '1,63\n', '34,77\n', '36,40\n', '0124 692544/03\n', '15.02.24 18:55'])


def test__extract_list_of_lines_after_total__rr(file_path):
    assert extract_list_of_lines_after_total(file_path, ['Sum', 'Amount', 'Grand Total']) is None


def test__get_max_number__return_max_number_from_the_list():
    assert get_max_number([1.0, 2.0, 3.9, 4.0]) == 4.0
