import datetime
import os
import pytest
from faker import Faker

from receipts.text_to_sum import extract_total_lines


# @pytest.fixture()
# def file_path() -> str:
#     path_to_file = 'test.txt'
#     with open(path_to_file, 'w') as file_handler:
#         file_handler.writelines(['0,00\n2,27\n2,27\nTotal\n1,63\n34,77\n36,40\n0124 692544/03\n15.02.24 18:55'])
#     yield path_to_file
#     os.remove(path_to_file)

# from unittest.mock import mock_open, patch


# @pytest.fixture
# def file_path():
#     m = mock_open()
#     with patch('__main__.open', m):
#         with open('test.txt', 'w') as file_handler:
#             b = file_handler.writelines(['0,00\n2,27\n2,27\nTotal\n1,63\n34,77\n36,40\n0124 692544/03\n15.02.24 18:55'])
#         return file_handler


NOT_SET = '___'
# faker = Faker
@pytest.fixture
def make_receipt(faker):
    faker = Faker

    def inner(total_part: str = NOT_SET):
        title_part = 'Test title'
        items_part = 'milk - 100.00\n, bread - 50.22\n'
        total_part = faker.pystr(150.22) if total_part is NOT_SET else total_part
        end_part = str(datetime.datetime.now().date())
        return '\n'.join([title_part, items_part, total_part, end_part])

    return inner



