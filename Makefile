format:
	cd dags/etl && python -m black -S --line-length 79 .

isort:
	cd dags/etl && isort .

type:
	cd dags/etl/bronze && mypy --ignore-missing-imports extract_api.py

lint:
	flake8 dags

check:
	make isort 
	make format 
	make type 
	make lint