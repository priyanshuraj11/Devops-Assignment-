# DevOps Lab 4 — Advanced Deployment Strategies

This project demonstrates enterprise DevOps practices using Jenkins, Docker, Kubernetes, and Argo CD.

## Technologies
- Python, Flask, Pytest
- Jenkins CI/CD
- Docker and Docker Compose
- Nginx
- Kubernetes (Minikube)
- Argo CD

## Lab Questions

| Question | Topic |
|---|---|
| Q1 | Automated testing and deployment gates |
| Q2 | Blue-Green deployment |
| Q3 | Canary deployment and rollback |
| Q4 | GitOps using Argo CD |
| Q5 | Secure secret management |
| Q6 | Disaster recovery and failover |
| Q7 | Advanced deployment strategies report |

## Run Tests

    python3 -m venv .venv
    .venv/bin/pip install -r requirements.txt
    .venv/bin/python -m pytest -v

## Blue-Green Deployment

    docker compose -f bluegreen/compose.yaml up -d
    curl http://localhost:8086/

## Canary Deployment

    docker compose -f canary/compose.yaml up -d
    curl http://localhost:8087/

## GitOps

Kubernetes manifests are available in `gitops/manifests/`.

Argo CD automatically synchronizes the deployment with GitHub.

## Secret Management

Jenkins Credentials and Kubernetes Secrets are used to inject credentials without exposing their values.

## Disaster Recovery

The `disaster-recovery/` directory contains Kubernetes manifests for persistent storage and recovery testing.

## Report

See [REPORT.md](REPORT.md) for the complete lab report.
