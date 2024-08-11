from flask import Flask, session
from prometheus_client import Counter, Gauge, generate_latest, start_http_server

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Metrics
active_sessions = Gauge('active_sessions', 'Number of active user sessions')

@app.before_request
def before_request():
    if 'user_id' not in session:
        session['user_id'] = 'user_{}'.format(id(session))
        active_sessions.inc()

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    active_sessions.dec()
    return "Logged out"

@app.route('/')
def hello():
    return "Hello, World!"

@app.route('/metrics')
def metrics():
    return generate_latest(), 200

if __name__ == '__main__':
    start_http_server(8000)  # Prometheus metrics server
    app.run(host='0.0.0.0', port=8080)  # Flask web server
