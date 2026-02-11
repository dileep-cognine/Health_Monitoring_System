# System Health Monitoring & Analytics Platform


A secure, scalable, and real-time system monitoring platform built using advanced Python concepts, asynchronous programming, and cloud-native deployment practices.

---

## Overview

This project monitors system metrics asynchronously, processes and analyzes data efficiently, triggers alerts based on configurable thresholds, and supports secure containerized and Kubernetes-based deployment.

---

## Architecture & Design Patterns

| Pattern      | Purpose |
|--------------|----------|
| **Singleton** | Configuration management |
| **Factory** | Processor creation |
| **Observer** | Alert notifications |
| **Strategy** | Flexible storage handling |
| **Async I/O** | Real-time metric collection |

---

## Performance Optimizations

- Generator-based file processing (O(1) memory usage)
- Asynchronous I/O using `asyncio` and `aiohttp`
- WeakRef caching to prevent memory leaks

---

## 🔐 Security Features

- Salted SHA-256 password hashing
- Fernet encryption for sensitive data
- Path traversal protection
- Secure configuration handling

---

## Testing

- Unit and async testing using `pytest`
- Full coverage of `src/` logic

Run tests:

```bash
pytest -v
```

---

# ▶️ Running the Application

## 🔹 Run Locally (Without Docker)

```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

python -m src.app
```

---

## Run with Docker (Single Container)

```bash
docker build -t monitoring-system -f deployment/Dockerfile .
docker run -d --name monitoring-app monitoring-system
```

Check logs:

```bash
docker logs -f monitoring-app
```

---

## Run with Docker Compose

```bash
docker compose -f deployment/docker-compose.yml up --build
docker compose -f deployment/docker-compose.yml down
```

---

## Kubernetes Deployment

Enable Kubernetes in Docker Desktop, then run:

```bash
kubectl get nodes
kubectl apply -f deployment/k8s/
kubectl get pods
kubectl logs deployment/monitoring-system
kubectl delete -f deployment/k8s/
```

---

# 📁 Project Structure

```
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
```

---

## Key Highlights

- Real-time async monitoring
- Secure architecture
- Docker & Kubernetes ready
- Modular and scalable design
- Production-ready structure

---

## Future Enhancements

- Prometheus integration
- Grafana dashboard
- OpenTelemetry tracing
- CI/CD pipeline setup
- Cloud deployment (AWS/GCP/Azure)

---

## Author

**Dileep Samaji**  
Software Engineer | AI & ML Enthusiast | Cloud & DevOps Learner
