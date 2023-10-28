PYTHON = python
SRC_DIR = src
TEST_DIR = tests
VENV_NAME = venv
REQUIREMENTS = requirements.txt

venv:
	if not exist $(VENV_NAME) $(PYTHON) -m venv $(VENV_NAME)
	
activate:
	$(VENV_NAME)\Scripts\activate

install: venv
	$(VENV_NAME)\Scripts\pip install -r $(REQUIREMENTS)

test: venv
	$(VENV_NAME)\Scripts\python -m unittest discover -s $(TEST_DIR) -p 'test_main.py'

run: venv
	$(VENV_NAME)\Scripts\python $(SRC_DIR)\main.py

clean:
	rmdir /S /Q $(VENV_NAME)
	del /Q /S __pycache__

.PHONY: venv install test run clean
