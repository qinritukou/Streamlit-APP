.PHONY: build_docker
build_docker:
	docker build -t irisedaapp:latest .

.PHONY: run_docker
run_docker:
	docker run -p 80:8501 irisedaapp:latest