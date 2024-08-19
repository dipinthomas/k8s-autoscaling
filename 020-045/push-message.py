import pika

# Define RabbitMQ server credentials
rabbitmq_host = '127.0.0.1'  # Replace with your RabbitMQ server host
rabbitmq_port = 5672         # Default RabbitMQ port
rabbitmq_user = 'user'      # Default RabbitMQ username
rabbitmq_password = 'eD6MVBwWF5wB743h'  # Default RabbitMQ password

# Define queue name
queue_name = 'dipin'

# Define the message to send
message = 'Hello, RabbitMQ!'


# Create a connection to RabbitMQ server
credentials = pika.PlainCredentials(rabbitmq_user, rabbitmq_password)
connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host, port=rabbitmq_port, credentials=credentials))
channel = connection.channel()

# Declare the queue (creates the queue if it doesn't exist)
channel.queue_declare(queue=queue_name, durable=True)

# Publish 100 messages to the queue
for i in range(1, 101):
    message = f'Message {i}'
    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          body=message,
                          properties=pika.BasicProperties(
                             delivery_mode=2,  # Make message persistent
                          ))
    print(f"Sent '{message}' to queue '{queue_name}'")

# Close the connection
connection.close()
