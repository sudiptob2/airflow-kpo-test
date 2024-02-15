# Testing Pod Event Log for Airflow KPO

To use this Makefile, you can run the following commands:  
- `make build VERSION=<version>` to build the Docker image.
- `make push VERSION=<version>` to push the Docker image to the repository.
- `make deploy VERSION=<version>` to deploy the Helm chart.
- `make uninstall` to uninstall the Helm chart.

Please replace `<version>` with the version you want to use for the Docker image.