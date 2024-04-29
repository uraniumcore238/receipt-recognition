from fastapi import FastAPI
from pydantic import BaseModel
from receipts.text_to_sum import extract_total_lines, extract_totals, read_receipt

app = FastAPI()


class ResponseTotal(BaseModel):
    """Return total value from the receipt."""

    total: float


class Receipt(BaseModel):
    """Receipt model."""

    receipt_text: str


@app.post("/api/v1/extract-total")
def extract_total_from_text(text_from_receipt: Receipt) -> ResponseTotal:
    text = text_from_receipt.receipt_text
    list_of_strings_under_total = extract_total_lines(text)
    list_of_numbers = extract_totals(list_of_strings_under_total)
    total = max(list_of_numbers)
    return ResponseTotal(total=total)


@app.post("/api/v1/total_from_file")
def extract_total_from_file_path(receipt_path: str) -> ResponseTotal:
    receipt_text = read_receipt(receipt_path)
    list_of_strings_under_total = extract_total_lines(receipt_text)
    list_of_numbers = extract_totals(list_of_strings_under_total)
    total = max(list_of_numbers)
    return ResponseTotal(total=total)
