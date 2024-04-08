import os
import pytest


@pytest.fixture
def file_path():
    path_to_file = 'test.txt'
    with open(path_to_file, 'w') as file_handler:
        file_handler.writelines(['0,00\n2,27\n2,27\nTotal\n1,63\n34,77\n36,40\n0124 692544/03\n15.02.24 18:55'])
    yield path_to_file
    os.remove(path_to_file)
