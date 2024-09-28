format:
	cd dags/etl && python -m black -S --line-length 79 .

isort:
	cd dags/etl && isort .

type:
	mypy dags/etl/bronze/

lint:
	flake8 dags/etl/bronze/

check:
	isort format type lint