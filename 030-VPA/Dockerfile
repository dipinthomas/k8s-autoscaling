# Use an official Ubuntu as a parent image
FROM ubuntu:latest

# Update and install necessary packages
RUN apt-get update && apt-get install -y \
    procps \
    htop \
    && rm -rf /var/lib/apt/lists/*

# Set the command to keep the container running
CMD ["tail", "-f", "/dev/null"]
