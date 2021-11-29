from Broker import Broker as B
from Message import Message
from Publisher import Publisher as P
from Subscriber import Subscriber as S

if __name__ == '__main__':

    # Initialize a Broker and register a Topic.
    print("*************************************")
    broker = B("broker101")
    broker.register_topics("topic1")
    broker.register_topics("topic2")

    # Enforce a type of message

    m1 = Message("00001", "some value 1, topic 1")
    m2 = Message("00002", "some value 2, topic 1")
    m3 = Message("00003", "some value 3, topic 2")
    # initialize a publisher and register with Broker ..

    p1 = P(broker)
    p1.publish("topic1", message = m1)
    p1.publish("topic1", message = m2)

    p2 = P(broker)
    p2.publish("topic2", message= m3)
    
    # Initialize a Subscriber .. 
    
    s1 = S(broker= broker)
    s1.poll("topic1")
    s1.poll("topic2")

    print("*************************************")

    m4= Message("00004", "some value 4, topic 2")
    m5 = Message("00005", "some value 5, topic 2")

    p1.publish("topic1", message=m4)
    p2.publish("topic2", message=m4)
    p2.publish("topic2", message=m5)

    s1.poll("topic1")
    s1.poll("topic2")

