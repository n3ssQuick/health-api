.PHONY: all init run test build clean

all: init test run

init:
	pip install -r requirements.txt

run:
	python app.py

test:
	pytest -v -s test/test_health_utils.py
	pytest -v -s test/test_api_endpoints.py
	
build:
	docker build -t health-calculator .
	docker run -d -p 9000:9000 --name health-calculator health-calculator

clean:
	rm -rf __pycache__
	docker stop health-calculator | docker rm health-calculator