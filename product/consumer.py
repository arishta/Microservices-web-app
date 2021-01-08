import pika
import json
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "product.settings")
django.setup()
from ProductInfo.models import Product


params = pika.URLParameters(
    'amqps://odanfvdh:AJUyQ07Lylr9Oe_G4YlzU0nO_W4vdIW9@lionfish.rmq.cloudamqp.com/odanfvdh')


connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='product')


def callback(ch, method, properties, body):
    print('Received in product')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')


channel.basic_consume(
    queue='product', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
