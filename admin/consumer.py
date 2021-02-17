import pika

params = pika.URLParameters('amqps://gwmgwwlo:FODPgdJZCfCBZ4qnd70PlRs9RjLCB0Qc@shark.rmq.cloudamqp.com/gwmgwwlo')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch,method,propperties,body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='admin',on_message_callback=callback,auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
