import pika
import secret

credentials = pika.PlainCredentials(secret.username, secret.password)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', 5672, '/test', credentials))
channel = connection.channel()

channel.queue_declare(queue='post.create')

def callback(ch, method, properties, body):
  print("[x] Received %r" % body)

channel.basic_consume(queue='post.create', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()