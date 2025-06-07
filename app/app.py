from flask import Flask
from prometheus_flask_exporter import PrometheusMetrics
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route("/")
def home():
    return "Hello from Flask in Kubernetes!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
