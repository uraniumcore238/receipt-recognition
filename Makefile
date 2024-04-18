ifeq (,$(wildcard .env))
	$(info Found .env file.)
	include .env
	export
endif

style:
	ruff .

types:
	mypy receipt-recognition

tests:
	pytest .

check:
	make -j3 style types tests
    
