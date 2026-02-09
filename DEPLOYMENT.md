# Deployment Guide

## Docker Build
```bash
docker build -t monitoring-system -f deployment/Dockerfile .

## Kubernetes Deployment

```bash
kubectl apply -f deployment/k8s/configmap.yaml
kubectl apply -f deployment/k8s/secret.yaml
kubectl apply -f deployment/k8s/deployment.yaml
kubectl apply -f deployment/k8s/service.yaml
kubectl apply -f deployment/k8s/hpa.yaml
