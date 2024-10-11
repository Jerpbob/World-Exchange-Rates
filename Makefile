format:
	cd dags/etl && python -m black -S --line-length 79 .

isort:
	isort dags/etl/

type:
	cd dags/ && mypy --ignore-missing-imports etl/transform/lambda/python/list_s3_objects.py

lint:
	flake8 dags

check:
	make isort 
	make format 
	make type 
	make lint