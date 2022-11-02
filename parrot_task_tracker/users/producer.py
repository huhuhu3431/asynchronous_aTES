import pika

params = pika.URLParameters('amqps://sxusatsv:ARr_mAf-OsmwawP0MIguGUZflTRMzBRo@hawk.rmq.cloudamqp.com/sxusatsv')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='admin', body='hello')