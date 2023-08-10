.PHONY activate_message:
activate_message:
	@echo
	@echo "---------------------------------------------------------------------"
	@echo "------ Run: 'source venv/bin/activate' to activate virtual env ------"
	@echo "---------------------------------------------------------------------"
	@echo

.PHONY venv:
venv:
	python3 -m venv venv;

.PHONY setup:
setup: venv
	. venv/bin/activate; \
	pip install -r requirements-dev.txt; \
	make activate_message

.PHONY clean_venv:
clean_venv:
	rm -rf venv

.PHONY test:
test:
	pytest
