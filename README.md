# 📦 DevOps Monitoring App with Flask, Kubernetes, Prometheus & Grafana
This project demonstrates how to deploy a simple Python Flask API in Kubernetes and monitor it using Prometheus and Grafana, configured via Helm.

## 📁 Project Structure
``` 
├── dockerfile                      # Dockerfile for Flask API
├── flask-api/                     # Flask API source code
│   ├── app.py
│   └── requirements.txt
├── k8s/
│   ├── flask-deployment.yaml      # Kubernetes Deployment & Service for Flask API
│   ├── frontend-deployment.yaml   # (Optional) Frontend app setup
│   └── monitoring-values.yaml     # Custom Prometheus + Grafana Helm config
├── kind-config.yaml               # Kind cluster configuration (if used)
└── README.md
```

## 🚀 Features
- ✅ Flask API containerized with Docker

- ✅ Deployed to Kubernetes using kubectl

- ✅ Metrics exported with prometheus_flask_exporter

- ✅ Prometheus configured to scrape metrics

- ✅ Grafana dashboards to visualize API health

- ✅ Metrics exposed: request counts, latency, uptime, etc.

## 🛠️ Stack
- Python Flask

- Docker

- Kubernetes (with Kind or Minikube)

- Prometheus + Grafana (via Helm chart)

- Helm: kube-prometheus-stack

## 🧪 How to Run
### 1. ✅ Clone and build Flask app
```
git clone https://github.com/davmano/devops-app.git
cd your-repo
```
```
docker build -t davmano/flask-api:latest .
docker push davmano/flask-api:latest
``` 
### 2. 🧱 Create Kind Cluster (if using Kind)
```
kind create cluster --config kind-config.yaml
``` 
### 3. 🚢 Deploy Flask app to Kubernetes
```
kubectl apply -f k8s/flask-deployment.yaml
```

### 4. 📡 Install Prometheus + Grafana with Helm
``` 
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
```
```
helm install monitoring prometheus-community/kube-prometheus-stack \
  -f k8s/monitoring-values.yaml \
  --namespace devops-app --create-namespace
``` 
### 5. 🔌 Expose Prometheus + Grafana
``` 
kubectl port-forward svc/monitoring-grafana 3000:80 -n devops-app
kubectl port-forward svc/monitoring-kube-prometheus-prometheus 9090:9090 -n devops-app
``` 
Grafana: http://localhost:3000

Prometheus: http://localhost:9090

Default Grafana login: admin / prom-operator

## 📊 Metrics Observed

`http_request_duration_seconds_count` 

`werkzeug_request_total`

`up{job="flask-api"}`

## 📈 Dashboards

`Import this dashboard in Grafana:`

-  Dashboard ID: `14057` (Flask Prometheus Exporter)

Or create a new one and use PromQL queries like:

```
http_request_duration_seconds_count{job="flask-api"}
werkzeug_request_total{job="flask-api"}
``` 
