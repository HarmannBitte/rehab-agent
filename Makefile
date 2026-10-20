# Convenience wrappers — all logic lives in scripts/*.py (stdlib only)
.PHONY: validate generate list-core clone-core status
validate:
	python3 scripts/validate_catalog.py
generate:
	python3 scripts/generate_catalog.py
list-core:
	python3 scripts/list.py --tier core
clone-core:
	python3 scripts/clone.py --tier core
status:
	python3 scripts/status.py
