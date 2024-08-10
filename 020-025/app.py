from flask import Flask
from prometheus_client import Counter, generate_latest, start_http_server

app = Flask(__name__)

# Create a counter metric to track the number of HTTP requests
http_requests_total = Counter('http_requests_total', 'Total HTTP Requests')

@app.route('/')
def hello():
    http_requests_total.inc()  # Increment the counter on each request
    return "Hello, World!"

@app.route('/metrics')
def metrics():
    # Expose the metrics to be scraped by Prometheus
    return generate_latest(), 200

if __name__ == '__main__':
    # Start Prometheus metrics server on port 8000
    start_http_server(8000)
    # Start the Flask app on port 8080
    app.run(host='0.0.0.0', port=8080)
