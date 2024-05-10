import datetime
from unittest.mock import patch

import pytest

from faker import Faker


NOT_SET = '___'


@pytest.fixture
def make_receipt(faker, today_date):
    faker = Faker()

    def inner(total_part: str = NOT_SET) -> str:
        title_part = 'Test title receipt'
        items_part = 'milk - 100.00\n, bread - 50.22\n'
        if total_part is NOT_SET:
            total_part = faker.pystr(min_chars=10, max_chars=15, suffix='total 150.15')
        end_part = str(today_date)
        return f'{title_part}\n{items_part}\n{total_part}\n{end_part}'

    return inner


@pytest.fixture
def extract_total_lines_mock():
    with patch('receipts.text_to_sum.extract_total_lines') as mock:
        yield mock


@pytest.fixture
def today_date():
    return datetime.datetime.now().date()

@pytest.fixture
def filepath():
    return "filepath"
