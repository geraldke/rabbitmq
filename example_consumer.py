from classes.consumer import Consumer

print "Waiting for messages.."

consumer = Consumer('analytics')
consumer.consume('events', 'greetings')
