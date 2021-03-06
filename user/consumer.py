import pika
import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user.settings")
django.setup()

from UserInfo.models import User

params = pika.URLParameters(
    'amqps://odanfvdh:AJUyQ07Lylr9Oe_G4YlzU0nO_W4vdIW9@lionfish.rmq.cloudamqp.com/odanfvdh')


connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='user')


def callback(ch, method, properties, body):
    print('Received in user')
    id = json.loads(body)
    print(id)
    user = User.objects.get(id=id)
    user.products_liked += 1
    user.save()
    print('user likes increased!')


channel.basic_consume(
    queue='user', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
