import pika

def callback(ch, method, properties, body):
    print(" [x] Recieved %r" % body)


def main():
    credentials = pika.PlainCredentials('mqadmin', 'mqadmin')
    parameters = pika.ConnectionParameters('80.87.198.203', 5672, '/', credentials)
    connection = pika.BlockingConnection(parameters)

    channel = connection.channel()

    channel.queue_declare(queue='queue1')

    channel.basic_consume(queue='queue1', on_message_callback=callback, auto_ack=True)

    print(' [x] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

main()