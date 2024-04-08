from app.total_from_receipt import total_from_receipt


def test__total_from_receipt__return_total_sum_of_the_receipt(file_path):
    assert total_from_receipt(file_path) == 36.4


