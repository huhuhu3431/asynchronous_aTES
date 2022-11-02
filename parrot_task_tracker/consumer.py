import pika

params = pika.URLParameters('amqps://sxusatsv:ARr_mAf-OsmwawP0MIguGUZflTRMzBRo@hawk.rmq.cloudamqp.com/sxusatsv')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def callback(ch, method, properties, body):
    print('message received, body:')
    print(body)

channel.basic_consume(queue='admin', on_message_callback=callback)

print('started consuming')

channel.start_consuming()

channel.close()