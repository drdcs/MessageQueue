from Broker import Broker


class Subscriber():
    """A Subscriber , polls the topic and get message from the broker."""
    def __init__(self, broker: Broker):
        self.broker = broker

    def poll(self, topic):
        if topic not in self.broker.broker_dict:
            print(topic, " topic is not registered")
        else:
            while len(self.broker.broker_dict[topic]) > 0:
                x = self.broker.broker_dict[topic].pop(0)
                print(x)