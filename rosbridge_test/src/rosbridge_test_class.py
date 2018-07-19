import rospy
from std_msgs.msg import String


class ROSBridgeTest(object):

    def __init__(self, subscribing_topic, publishing_topic):

        rospy.Subscriber(subscribing_topic, String, self.callback)
        self.pub = rospy.Publisher(publishing_topic, String, queue_size=10, latch=True)
        rospy.sleep(1)
        self.publish_input()

    @staticmethod
    def callback(msg):
        print ('')
        print ('Received message: ' + msg.data)

    def publish_input(self):
        msg = String()
        msg.data = raw_input('Message to send: ')

        if msg.data == 'exit()':
            quit()
        else:
            self.pub.publish(msg)
            self.publish_input()
