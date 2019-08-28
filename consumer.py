import pika
import secret
import slackPostman as sp

credentials = pika.PlainCredentials(secret.username, secret.password)
connection = pika.BlockingConnection(pika.ConnectionParameters(
  host = 'localhost', 
  port = 5672, 
  virtual_host = 'test', 
  credentials = credentials
  ))
channel = connection.channel()

def callback(ch, method, properties, body):
  sp.send("[x] Received %r" % body)

channel.basic_consume(queue='post.create', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()