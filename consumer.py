import pika

connection = pika.BlokingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='post.create')

def callback(ch, method, properties, body):
  print("[x] Received %r" % body)

channel.basic_consume(queue='post.create', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()