from classes.producer import Producer

producer = Producer('analytics')
producer.publish('Hello there', 'greetings')