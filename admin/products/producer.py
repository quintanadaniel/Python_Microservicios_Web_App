import pika,json

params = pika.URLParameters('amqps://gwmgwwlo:FODPgdJZCfCBZ4qnd70PlRs9RjLCB0Qc@shark.rmq.cloudamqp.com/gwmgwwlo')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method,body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='',routing_key='main',body=json.dumps(body),properties=properties)