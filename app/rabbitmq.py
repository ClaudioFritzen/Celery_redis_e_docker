"""import pika
import json


def publish_user_created(user_id:int, email:str):

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq')
    )

    channel = connection.channel()

    channel.exchange_declare(exchange='user_events', exchange_type='topic')

    payload = {
        'user_id': user_id,
        'email': email,
        'action': 'verify_email'
    }

    channel.basic_publish(
        exchange='user_events',
        routing_key='user.created',
        body=json.dumps(payload)
    )

    connection.close()"""