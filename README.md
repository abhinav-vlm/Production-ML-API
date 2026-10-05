Production ML API

1. Project Purpose

This project is a learning-focused production ML engineering laboratory.

The ML model is intentionally simple. The primary objective is to learn how to take a trained ML model and turn it into a reliable, tested, containerized, deployable, observable production service.

The project should maximize learning in:

- Backend/API engineering
- ML inference engineering
- Testing
- Configuration management
- Logging
- Docker
- CI/CD
- AWS
- Cloud deployment
- Kubernetes
- Monitoring and observability
- Model/version management
- Production engineering practices

The ML component exists primarily to provide a realistic artifact that must be served in production.

---

2. Core Principle

«Keep ML small. Maximize production/MLOps learning.»

The project must NOT become another ML experimentation project.

Do not spend significant time on:

- Hyperparameter tuning
- Complex feature engineering
- Large datasets
- Advanced model architectures
- Model competitions
- Squeezing out tiny accuracy improvements
- Research-level ML optimization

The Iris classification model is sufficient for the ML foundation.

The impressive part of this project is:

Trained Model
      ↓
Inference Layer
      ↓
Tested API
      ↓
Docker Container
      ↓
CI
      ↓
Container Registry
      ↓
AWS Deployment
      ↓
CD
      ↓
Kubernetes
      ↓
Monitoring

---

3. Relationship With AAA Resume Intelligence Platform

Project A is a supporting learning project.

AAA Resume Intelligence Platform remains the primary portfolio project.

Project A exists to close production engineering gaps so that the same concepts can later be applied to AAA without stopping the main project to learn infrastructure fundamentals.

Examples:

Project A
FastAPI
Docker
pytest
CI/CD
AWS
Kubernetes
logging
health checks
monitoring

             ↓

AAA
Production deployment
API engineering
MLOps
observability
CI/CD
cloud infrastructure

Project A should therefore optimize for transferable engineering knowledge, not portfolio complexity.

---

4. Current ML Model

Dataset:

Iris

Model:

Logistic Regression

Current artifact:

models/iris_classifier.joblib

Current ML work completed:

- Dataset loading
- Feature/target understanding
- Train/test split
- Logistic Regression training
- Evaluation
- Accuracy
- Classification report
- Confusion matrix
- Model serialization
- Model loading
- Basic inference experimentation

The ML foundation is considered sufficient.

---

5. Production Architecture

Target architecture:

                    ┌─────────────────┐
                    │   Client/User   │
                    └────────┬────────┘
                             │ HTTP
                             ↓
                    ┌─────────────────┐
                    │    FastAPI      │
                    │                 │
                    │ /predict        │
                    │ /health         │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Input Validation│
                    │ + API Contract  │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Inference Layer │
                    └────────┬────────┘
                             ↓
                    ┌─────────────────┐
                    │ Model Artifact  │
                    │ .joblib         │
                    └─────────────────┘

This application will then be packaged:

Application
     ↓
Docker Image
     ↓
Container Registry
     ↓
AWS
     ↓
Kubernetes
     ↓
Production Service

---

6. Phase Roadmap

Phase 1 — ML Foundation

Purpose: Create the smallest possible usable ML artifact.

Tasks:

- Choose simple tabular problem
- Load dataset
- Define features and target
- Train/test split
- Train model
- Evaluate model
- Save model artifact
- Understand what inference requires

Status:

COMPLETE

---

Phase 2 — Inference Layer

Purpose: Separate model inference from training.

Tasks:

- Load model safely
- Create prediction function
- Define input contract
- Validate inputs
- Preserve feature ordering
- Return structured prediction
- Handle invalid inputs
- Write unit tests

Important principle:

Application Input
       ↓
Validation
       ↓
Feature Ordering
       ↓
Model
       ↓
Prediction

ML complexity should remain minimal.

Status:

IN PROGRESS

---

Phase 3 — FastAPI

Purpose: Turn the inference layer into a proper HTTP service.

Tasks:

- FastAPI application
- Application structure
- Pydantic request models
- Pydantic response models
- POST "/predict"
- GET "/health"
- HTTP status codes
- Validation errors
- Application error handling
- API testing
- OpenAPI documentation

Target:

POST /predict
GET  /health

The API should call the inference layer rather than contain model logic itself.

---

Phase 4 — Engineering

Purpose: Make the application maintainable.

Tasks:

- Proper project structure
- Python package structure
- Configuration management
- Environment variables
- ".env" for local development where appropriate
- Logging
- Exception handling
- Dependency management
- pytest
- Unit tests
- Integration/API tests
- Test organization

Target separation:

API
 ↓
Service / Inference
 ↓
Model

No giant "main.py" containing the entire application.

---

Phase 5 — Docker

Purpose: Learn containerization properly.

Tasks:

- Understand containers vs virtual environments
- Write Dockerfile
- Build image
- Run container
- Port mapping
- Environment variables
- Container filesystem
- ".dockerignore"
- Image inspection
- Container logs
- Test API inside container
- Optimize basic image structure

Target:

Source Code
    ↓
Dockerfile
    ↓
Docker Image
    ↓
Container
    ↓
FastAPI

---

Phase 6 — CI

Purpose: Automate quality checks.

Use GitHub Actions.

Pipeline should eventually perform:

git push
   ↓
CI starts
   ↓
Install dependencies
   ↓
Run tests
   ↓
Run quality checks
   ↓
Build Docker image

Topics:

- GitHub Actions
- Workflows
- Jobs
- Steps
- Secrets
- Environment variables
- Test automation
- Docker build automation

---

Phase 7 — AWS

Purpose: Learn the cloud infrastructure required to operate the service.

Topics to cover:

- AWS fundamentals
- IAM
- Permissions
- ECR
- Container image lifecycle
- Compute
- Networking fundamentals
- Security groups
- Environment configuration
- Secrets
- Logs
- Health checks

The project should use AWS as a practical learning environment rather than attempting to learn every AWS service ever invented.

---

Phase 8 — CD

Purpose: Automate deployment.

Target lifecycle:

git push
   ↓
CI
   ↓
Tests
   ↓
Docker build
   ↓
Push image to ECR
   ↓
Deployment
   ↓
Health check

Topics:

- Deployment automation
- Image tagging
- Versioning
- Environment separation
- Deployment failure handling
- Rollback concepts

---

Phase 9 — Kubernetes

Purpose: Understand container orchestration.

Topics:

Core concepts

- Cluster
- Node
- Pod
- Deployment
- Service
- Namespace

Configuration

- ConfigMap
- Secret

Production behavior

- Readiness probe
- Liveness probe
- Resource requests/limits
- Replicas
- Rolling deployment
- Scaling
- Service discovery

Target:

Kubernetes
    │
    ├── Deployment
    │      └── Pods
    │
    ├── Service
    │
    ├── ConfigMap
    │
    ├── Secret
    │
    └── Health Probes

The goal is understanding why each primitive exists, not memorizing YAML.

---

Phase 10 — Observability

Purpose: Understand how production systems are monitored.

Tasks:

- Application logging
- Container logs
- Health endpoints
- Readiness/liveness checks
- Basic metrics
- Request latency
- Error tracking
- Model prediction monitoring
- Basic operational dashboards where practical

Important distinction:

Logging
→ What happened?

Metrics
→ How often/how much?

Health checks
→ Is the service alive and ready?

Monitoring
→ Is the system behaving normally?

---

Phase 11 — Model Lifecycle / MLOps

Once the infrastructure is understood, introduce the ML-specific production lifecycle.

Target:

Data
 ↓
Validation
 ↓
Training
 ↓
Evaluation Gate
 ↓
Model Artifact / Registry
 ↓
Deployment
 ↓
Inference
 ↓
Monitoring
 ↓
Drift / Performance Signal
 ↓
Retraining
 ↓
Redeployment

Potential tooling should be introduced only when the underlying concept is understood.

Model/version management should be treated as a production concern rather than an excuse to add seventeen fashionable tools.

---

Phase 12 — Documentation

Final documentation should include:

- Architecture diagram
- Project structure
- API documentation
- Local setup
- Environment configuration
- Docker instructions
- Testing instructions
- CI/CD workflow
- AWS architecture
- Kubernetes architecture
- Deployment instructions
- Monitoring approach
- Design decisions
- Trade-offs
- Known limitations
- Failure/rollback strategy

---

7. Learning Rules

Rule 1 — ML stays small

Do not expand the Iris model unless it teaches an important production concept.

---

Rule 2 — Understand before frameworks

Before using a tool, understand the problem it solves.

Examples:

Docker
→ What problem does containerization solve?

Kubernetes
→ What problem does orchestration solve?

CI/CD
→ What problem does automation solve?

AWS
→ What infrastructure problem are we solving?

Model registry
→ What model lifecycle problem are we solving?

---

Rule 3 — Build, don't watch

Every major topic must involve implementation.

Concept
 ↓
Implement
 ↓
Break it
 ↓
Debug it
 ↓
Test it
 ↓
Understand it

---

Rule 4 — No giant code dumps

Implementation should be incremental.

The workflow is:

Concept
 ↓
Requirement
 ↓
User implementation
 ↓
Review
 ↓
Correction
 ↓
Test
 ↓
Next component

---

Rule 5 — One layer at a time

Do not introduce:

FastAPI + Docker + Kubernetes + AWS

simultaneously.

Build the dependency chain:

Python
 ↓
Inference
 ↓
API
 ↓
Tests
 ↓
Docker
 ↓
CI
 ↓
AWS
 ↓
CD
 ↓
Kubernetes
 ↓
Monitoring

---

8. Session Constraint

Each Project A session should target approximately 1 hour minimum, with longer sessions used when the topic genuinely benefits from it.

Preferred structure:

10–15 min
Concept

30–35 min
Implementation

10–15 min
Testing / debugging / reasoning

Do not artificially add work merely to fill time.

However, a major infrastructure topic should be allowed to occupy multiple sessions when necessary.

---

9. Priority Allocation

Approximate learning emphasis:

ML Foundation / Inference     ███
FastAPI                       ████
Testing                       ████
Engineering                   ████
Docker                        █████
CI/CD                         █████
AWS                           █████
Kubernetes                    █████
Observability                 ████
Model Lifecycle / MLOps      █████

The project should not become:

████████████████ ML experimentation
██ Docker
█ AWS

It should be the opposite.

---

10. Definition of Done

Project A is successful when we can demonstrate:

1. A trained model exists
2. The model is loaded by an inference service
3. The inference layer is tested
4. FastAPI exposes the model
5. API validation works
6. Application logging works
7. Automated tests run in CI
8. The application is containerized
9. Docker image is built automatically
10. Image is stored in AWS
11. Application is deployed to AWS
12. CD can deploy a new version
13. Application runs under Kubernetes
14. Kubernetes manages replicas/configuration/secrets
15. Health probes work
16. Logs and basic metrics are observable
17. Model/version lifecycle is understood
18. The entire architecture can be explained without reading the README

---

11. Explicit Non-Goals

This project is not intended to become:

- An ML research project
- A Kaggle competition
- A complex prediction system
- A huge dataset pipeline
- A deep-learning project
- A generic CRUD application
- A Kubernetes certification course
- An AWS service catalog
- A collection of disconnected tutorials

The project must remain a small ML workload wrapped in an increasingly realistic production system.

---

12. Current Checkpoint

Project A
Production ML API

P1 ML Foundation
██████████ COMPLETE

P2 Inference Layer
██████░░░░ IN PROGRESS

P3 FastAPI
░░░░░░░░░░

P4 Engineering
░░░░░░░░░░

P5 Docker
░░░░░░░░░░

P6 CI
░░░░░░░░░░

P7 AWS
░░░░░░░░░░

P8 CD
░░░░░░░░░░

P9 Kubernetes
░░░░░░░░░░

P10 Observability
░░░░░░░░░░

P11 MLOps Lifecycle
░░░░░░░░░░

P12 Documentation
░░░░░░░░░░

Current artifacts:

models/
└── iris_classifier.joblib

Next implementation milestone:

Finish minimal inference layer
        ↓
Move immediately to FastAPI
        ↓
Shift project emphasis toward MLOps