import datetime
import pytest

from faker import Faker


NOT_SET = '___'


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
