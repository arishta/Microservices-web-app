import pika

import json

params = pika.URLParameters(
    'amqps://odanfvdh:AJUyQ07Lylr9Oe_G4YlzU0nO_W4vdIW9@lionfish.rmq.cloudamqp.com/odanfvdh')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='product',
                          body=json.dumps(body), properties=properties)


def publish2(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='user',
                          body=json.dumps(body), properties=properties)
