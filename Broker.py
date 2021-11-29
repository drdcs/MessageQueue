from collections import OrderedDict


class Broker:
    """Broker : communication layer between a publisher and a subscriber.
    """
    def __init__(self, name):
        self.topics = {}
        self.name = name
        self.broker_dict = OrderedDict()

    def register_topics(self, topic_name):
        """Register a topic to the broker."""
        if len(self.topics.keys()) == 0:
            self.topics[topic_name] = True
        else:
            if topic_name in self.topics.keys():
                print("topic with name ", topic_name, " already registered")
            else:
                self.topics[topic_name] = True

    def __repr__(self):
        return "broker " + self.name + " is in service" + " have " + self.topics
