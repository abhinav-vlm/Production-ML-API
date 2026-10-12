Production ML API

A learning-focused production ML engineering project that takes a small machine learning model from training through API development, testing, containerization, CI, and AWS deployment.

The goal is to keep the ML workload simple and focus on the engineering required to operate an ML service.

«Core principle: Keep ML small. Maximize production and MLOps learning.»

1. Project Objectives

This project is designed to build practical experience in:

- ML inference and API engineering
- Input validation and automated testing
- Configuration management and application structure
- Docker and Docker Compose
- Continuous integration and continuous delivery (CI/CD)
- AWS infrastructure and deployment
- Logging, health checks, and observability
- Model versioning and production ML lifecycle management

The Iris classifier is intentionally simple. The primary learning objective is the engineering system surrounding the model.

Project A is a supporting engineering project. The Resume Intelligence Platform remains the primary portfolio project.

2. Technology Stack

Component| Technology
Language| Python
ML model| Scikit-learn Logistic Regression
API| FastAPI
Request validation| Pydantic
Inference artifact| Joblib
Testing| pytest
Containerization| Docker
Local orchestration| Docker Compose
Reverse proxy and frontend| Nginx
Continuous integration| GitHub Actions
Cloud deployment| AWS EC2
Planned container registry| Amazon ECR
Planned automated deployment| GitHub Actions + AWS IAM/OIDC

3. Architecture

Current deployed architecture

Browser / Mobile Device
          |
          | HTTP :80
          v
     AWS EC2 Instance
          |
          v
     Nginx Frontend
          |
          | Docker internal network
          | /api/predict
          v
     FastAPI Backend
          |
          v
     Input Validation
          |
          v
     Inference Layer
          |
          v
     iris_classifier.joblib

The frontend and backend run as separate Docker Compose services.

Nginx serves the frontend and forwards "/api/" requests to the backend service. The backend listens on port 8000 inside the Docker network and is not directly exposed through an EC2 inbound rule.

Request lifecycle

1. The user enters four Iris measurements.
2. The frontend sends a JSON request to "/api/predict".
3. Nginx forwards the request to FastAPI.
4. FastAPI validates the request.
5. The inference layer loads and uses the trained model.
6. The API returns the prediction and probability.

4. Machine Learning Model

- Dataset: Iris
- Algorithm: Logistic Regression
- Model artifact: "models/iris_classifier.joblib"

The ML foundation includes data loading, feature and target selection, train/test splitting, model evaluation, serialization, and inference.

Further model experimentation is not a priority unless it teaches an important production engineering concept.

5. Repository Structure

.
├── .github/
│   └── workflows/
│       └── ci.yaml
├── frontend/
│   ├── Dockerfile
│   ├── app.js
│   ├── index.html
│   ├── nginx.conf
│   └── style.css
├── models/
│   └── iris_classifier.joblib
├── src/
│   ├── __init__.py
│   ├── inference.py
│   └── main.py
├── tests/
│   ├── test_api.py
│   └── test_inference.py
├── .dockerignore
├── .gitignore
├── compose.yaml
├── Dockerfile
├── requirements.txt
├── requirements-dev.txt
└── README.md

The repository structure may evolve as the project adds deployment automation and observability.

6. Local Development

Prerequisites

- Python 3.12
- Git
- Docker Desktop or Docker Engine with the Docker Compose plugin

Create a Python environment

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements-dev.txt

Configure the model path

The application supports a "MODEL_PATH" environment variable and has a default path to the model artifact.

For local configuration, create a ".env" file if required:

MODEL_PATH=models/iris_classifier.joblib

Do not commit ".env" files or secrets.

Run tests

pytest -q

The last recorded local test baseline was 9 passing tests, with one deprecation warning. Run the tests again to verify the current baseline.

Run the API locally

uvicorn src.main:app --reload

The API should be available at "http://localhost:8000".

Interactive API documentation is available at "/docs" when the application is running.

7. API Reference

Health check

GET /health

Returns the service health status.

Prediction endpoint

POST /predict
Content-Type: application/json

Example request:

{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}

Example response:

{
  "prediction": 0,
  "probability": 0.9784002314555064
}

The exact probability depends on the model artifact and inference implementation.

When using the Nginx frontend, the public-facing path is:

POST /api/predict

Nginx forwards this to the backend's "/predict" endpoint.

8. Docker Compose

Build and start both services:

docker compose up --build -d

The local frontend is available at:

http://localhost:8080

Inspect service status:

docker compose ps

View logs:

docker compose logs --tail 50

Stop the services:

docker compose down

The backend is accessible to the frontend through the internal Compose network. The backend port does not need to be published to the host for frontend-based predictions.

9. Continuous Integration

GitHub Actions runs automated tests on repository changes.

The CI workflow installs development dependencies and executes the test suite.

Current status: CI has passed in the previous verified run. Recheck the latest workflow run before treating a new commit as verified.

Automated Docker image publishing and AWS deployment are future milestones.

10. AWS Deployment

The application has been deployed to an AWS EC2 instance running Amazon Linux 2023.

Deployment architecture

- EC2 provides the compute environment.
- Docker runs the frontend and backend containers.
- Docker Compose manages the two services.
- Nginx serves the public frontend and proxies API requests.
- FastAPI serves predictions from the saved model artifact.

Security group

The intended inbound rules are:

Protocol| Port| Source| Purpose
SSH| 22| Restricted to the operator's IP| Administration
HTTP| 80| "0.0.0.0/0"| Public demo access

The backend's port 8000 is not exposed through an inbound security-group rule.

Security limitation: The public demo currently uses HTTP. Traffic is not encrypted. HTTPS and a valid TLS certificate remain future work.

Deployment verification

The deployed application has been tested from an external mobile device.

Verified behavior includes:

- Frontend returns HTTP 200.
- Prediction requests succeed through Nginx.
- The API returns a valid Iris prediction.
- Backend communication works over the internal Docker network.

Cost management

The EC2 instance should be stopped when the demo is not required. Stopping the instance reduces compute charges, but EBS storage and other applicable resources may still incur costs. The public IP may also change after stopping and restarting the instance.

11. Roadmap and Current Status

Phase| Objective| Status
1. ML foundation| Train and serialize the model| Complete
2. Inference| Validate input and run model inference| Implemented
3. FastAPI| Expose health and prediction endpoints| Implemented
4. Engineering| Tests, configuration and project structure| Core implemented
5. Docker| Containerize the application| Implemented
6. CI| Automate tests using GitHub Actions| Implemented
7. AWS| Deploy the service to EC2| Initial deployment verified
8. CD| Automate build, publishing and deployment| Next major milestone
9. Kubernetes| Learn orchestration and deployment primitives| Planned
10. Observability| Add metrics and operational monitoring| Planned
11. Model lifecycle| Add model versioning and lifecycle controls| Planned
12. Documentation| Document implementation and operational procedures| In progress

Status labels describe the current known implementation, not a claim that every production concern has been solved.

12. Next Milestone: Continuous Delivery

The next major objective is to remove manual image transfer and deployment steps.

Target workflow:

Git Push
   |
   v
GitHub Actions CI
   |
   v
Run Tests
   |
   v
Build Docker Images
   |
   v
Authenticate to AWS using IAM/OIDC
   |
   v
Push Images to Amazon ECR
   |
   v
Deploy Updated Images to EC2
   |
   v
Run Health Checks
   |
   v
Verify Deployment

Implementation will be incremental. First, the images will be published to ECR. Then AWS authentication and deployment automation will be configured, followed by failure handling and rollback concepts.

13. Learning Principles

1. Keep the ML workload small.
2. Understand the problem before introducing a tool.
3. Build and test instead of relying on tutorials alone.
4. Introduce one infrastructure layer at a time.
5. Debug failures and understand their causes.
6. Avoid giant code dumps and implement incrementally.
7. Prefer transferable engineering skills over unnecessary complexity.

14. Known Limitations

- The public demo currently uses HTTP rather than HTTPS.
- CD and automated image publishing have not yet been implemented.
- Kubernetes deployment has not yet been implemented.
- Production-grade metrics, alerting, and model monitoring remain future work.
- The Iris model is a learning artifact, not a production decision system.

15. Definition of Done

The broader learning project will be considered complete when the model is tested, the service is containerized, CI is automated, images are stored in a registry, deployment is automated, Kubernetes fundamentals are implemented, operational behavior is observable, and the complete architecture can be explained without relying on the README.

The objective is not to build a complex ML model. It is to demonstrate the engineering required to deploy, update, operate, and maintain an ML service.