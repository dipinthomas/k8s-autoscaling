#!/bin/bash

# Number of parallel requests
PARALLEL_REQUESTS=10

# Target URL
URL="http://flask-dispatch-service:8080"

# Function to send a single curl request
send_request() {
    while true; do
        curl -s $URL > /dev/null
    done
}

# Run the requests in parallel
for i in $(seq 1 $PARALLEL_REQUESTS); do
    send_request &
done

# Wait for all background jobs to finish
wait
