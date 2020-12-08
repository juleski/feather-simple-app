# Makefile for configuring and setting up the application
PHONY: clean

install:
	# Setting up backend
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt

clean:
	rm -rf .venv
