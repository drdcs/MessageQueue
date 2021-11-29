from Message import Message
from Broker import Broker


class Publisher():
    """:param: Takes Broker as a parameter"""

    def __init__(self, broker: Broker):
        self.broker = broker
        self.my_list = []

    def publish(self, topic, message: Message):
        """:param: topic: a topic registered in broker.
                   message: of type Message """
        self.my_list.append(message)
        if topic in self.broker.topics:
            self.broker.broker_dict[topic] = self.my_list
        else:
            print("Please check the topic, looks like topic not registered")
        return self.broker.broker_dict

    def show_message(self):
        return self.broker.broker_dict

    def __repr__(self):
        return self.broker.name + " is assigned to publisher "
