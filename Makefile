-include .env
export

style:
	ruff .

types:
	mypy receipts

tests:
	pytest .

check:
	make -j3 style types tests
