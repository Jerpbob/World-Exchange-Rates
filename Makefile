format:
	cd dags/etl && python -m black -S --line-length 79 .

isort:
	isort dags/etl/

type:
	cd dags/ && mypy --ignore-missing-imports etl/extract/invoke_lambda.py

lint:
	flake8 dags

check:
	make isort 
	make format 
	make type 
	make lint