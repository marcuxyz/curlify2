test:
	@pytest -vvv -s

check:
	@black . -l 80 --check

format:
	@black . -l 80

.PHONY: test check format
