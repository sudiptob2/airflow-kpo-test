# Makefile

# Variable for Docker image tag
VERSION ?= latest

# Docker image name
IMAGE_NAME = airflow_kpo_test

# Docker repository
DOCKER_REPO = localhost:5001

# Helm chart name
HELM_CHART = airflow

# Target to build Docker image
build:
	docker build -t $(DOCKER_REPO)/$(IMAGE_NAME):$(VERSION) ./dev

# Target to push Docker image to repository
push:
	docker push $(DOCKER_REPO)/$(IMAGE_NAME):$(VERSION)

# Target to deploy Helm chart
deploy:
	helm upgrade --install $(HELM_CHART) ./helm --set airflow.dags_image.tag=$(VERSION) --set airflow.dags_image.repository=$(DOCKER_REPO)/$(IMAGE_NAME)

# Target to uninstall Helm chart
uninstall:
	helm uninstall $(HELM_CHART)