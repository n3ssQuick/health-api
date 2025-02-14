.PHONY: init run test build clean

local: init test run
docker: build deploy

init:
	pip install -r requirements.txt

run:
	python app.py

test:
	pytest -v -s 
	
build:
	docker build -t health-calculator .

deploy:
	docker run -d -p 9000:9000 --name health-calculator health-calculator

clean:
	rm -rf __pycache__