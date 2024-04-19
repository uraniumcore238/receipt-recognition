ifeq (,$(wildcard .env))
	$(info Found .env file.)
	include .env
	export
endif

export PYTHONPATH :=$(shell pwd):$(PYTHONPATH)

style:
	ruff .

types:
	mypy receipt-recognition

tests:
	pytest .

check:
	make -j3 style types tests
    
