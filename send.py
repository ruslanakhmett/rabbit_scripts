import pika

def main():
    credentials = pika.PlainCredentials('mqadmin', 'mqadmin')
    parameters = pika.ConnectionParameters('80.87.198.203', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare(queue='queue1')

    while True:
        channel.basic_publish(exchange='', routing_key='queue1', body='Hello World')
        print(" [x] Sent 'Hello World!'")
    
    connection.close()

main()