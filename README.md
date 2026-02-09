# System Health Monitoring & Analytics Platform
This project implements a secure, real-time system monitoring and analytics platform using advanced Python concepts.
It monitors system metrics asynchronously, processes and analyzes data efficiently, triggers alerts based on thresholds, and supports secure, containerized, and Kubernetes-based deployment.
## Architecture Overview
- Singleton for configuration
- Factory for processor creation
- Observer for alerting
- Strategy for storage
- Async metrics collection
- Secure data handling

## Performance Optimizations
- Generator-based file processing (O(1) memory)
- Async I/O using asyncio & aiohttp
- WeakRef cache to avoid memory leaks

## Security Measures
- Salted SHA-256 password hashing
- Fernet encryption for sensitive data
- Path traversal protection in file I/O

## Testing
- Pytest for unit & async testing
- Full coverage of src/ logic

## Deployment
- Dockerized for reproducibility

# Project structure
monitoring-system/
├── src/
│   ├── app.py
│   ├── async_collectors/
│   ├── data_handlers/
│   ├── metaclasses/
│   ├── patterns/
│   ├── processors/
│   └── security/
├── tests/
├── profiling/
├── deployment/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── k8s/
│       ├── configmap.yaml
│       ├── deployment.yaml
│       ├── service.yaml
│       ├── secret.yaml
│       └── hpa.yaml
├── data/
├── requirements.txt
├── pytest.ini
├── DEPLOYMENT.md
└── README.md

# Run Commands
# Run Locally (Without Docker)
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

python -m src.app.py

# Run Tests
pytest -v

# Run with Docker (Single Container)
docker build -t monitoring-system -f deployment/Dockerfile .

# Check logs:
docker logs -f monitoring-app

# Run with Docker Compose
docker compose -f deployment/docker-compose.yml up --build
docker compose -f deployment/docker-compose.yml down

# Kubernetes Deployment
# Enable Kubernetes in Docker Desktop, then:

kubectl get nodes
kubectl apply -f deployment/k8s/
kubectl get pods
kubectl logs deployment/monitoring-system
kubectl delete -f deployment/k8s/
