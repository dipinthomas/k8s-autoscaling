from flask import Flask, request
from prometheus_client import start_http_server, Gauge
import time
import threading

app = Flask(__name__)

# Metric to expose
order_gauge = Gauge('order_count', 'Number of orders')

# In-memory store with TTL
order_count = 0
order_timestamp = time.time()

# Mutex to handle concurrency
lock = threading.Lock()

def reset_order_count():
    global order_count, order_timestamp
    while True:
        time.sleep(60)  # Check every minute
        with lock:
            if time.time() - order_timestamp > 300:  # 5 minutes = 300 seconds
                order_count = 0
                order_gauge.set(order_count)

@app.route('/orders', methods=['POST'])
def set_orders():
    global order_count, order_timestamp
    new_orders = request.json.get('orders', 0)
    
    with lock:
        order_count = new_orders
        order_timestamp = time.time()
        order_gauge.set(order_count)
    
    return {"status": "success", "order_count": order_count}

@app.route('/metrics')
def metrics():
    return Response(prometheus_client.generate_latest(), mimetype="text/plain")

if __name__ == "__main__":
    # Start Prometheus metrics server
    start_http_server(8000)
    
    # Start reset thread
    reset_thread = threading.Thread(target=reset_order_count)
    reset_thread.daemon = True
    reset_thread.start()
    
    # Start Flask application
    app.run(host='0.0.0.0', port=5000)
