from fastapi import FastAPI
from receipts.total_from_receipt import total_from_receipt

app = FastAPI()


@app.post("/extract_total/")
async def extract_total_from_text(file_path: str) -> float:
    return total_from_receipt(file_path)
