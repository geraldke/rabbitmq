import pika
import yaml

class Producer:
    def __init__(self,
                 exchange_name,
                 exchange_type='direct',
                 passive=False,
                 durable=True,
                 auto_delete=False):

        self.exchange_name = exchange_name
        self.exchange_type = exchange_type
        self.passive = passive
        self.durable = durable
        self.auto_delete = auto_delete

        self.__get_config()
        self.__connect()

    def publish(self, message, routing_key):
        self.channel.exchange_declare(exchange=self.exchange_name,
                                      type=self.exchange_type,
                                      passive=self.passive,
                                      durable=self.durable,
                                      auto_delete=self.auto_delete)
        self.channel.basic_publish(exchange=self.exchange_name,
                                   routing_key=routing_key,
                                   body=message,
                                   properties=pika.BasicProperties(
                                       delivery_mode = 2
                                   ))
        print "Message sent"
        self.connection.close()

    def __connect(self):
        user = self.config['rabbitmq']['user']
        password = self.config['rabbitmq']['password']
        host = self.config['rabbitmq']['host']
        port = self.config['rabbitmq']['port']
        credentials = pika.PlainCredentials(user, password)

        parameters = pika.ConnectionParameters(host, port, '/', credentials)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

    def __get_config(self):
        with open('config/default.yml', 'r') as f:
            self.config = yaml.load(f)