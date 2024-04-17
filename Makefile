style:
    ruff .

types:
    mypy receipt-recognition

tests:
    pytest .

check:
    make -j3 style types tests
    
