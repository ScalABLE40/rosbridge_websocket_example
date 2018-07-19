#!/usr/bin/env python

import websocket
import json

subscribing_topic = "/from_ros_node"
publishing_topic = "/to_ros_node"

try:
    import thread
except ImportError:
    import _thread as thread


def on_message(ws, message):
    print('Received message: ' + message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):

        advertise_message = {'op': 'advertise', 'topic': publishing_topic, 'type': 'std_msgs/String'}
        publish_message = {'op': 'publish', 'topic': publishing_topic, 'msg': {'data': 'websocket communication started'}}
        subscribe_message = {'op': 'subscribe', 'topic': subscribing_topic, 'type': 'std_msgs/String'}

        ws.send(json.dumps(advertise_message))
        ws.send(json.dumps(publish_message))
        ws.send(json.dumps(subscribe_message))

    thread.start_new_thread(run, ())


def publish_input(input_msg):
    publish_message = {'op': 'publish', 'topic': publishing_topic, 'msg': {'data': input_msg}}
    ws.send(json.dumps(publish_message))


def input_message():
    msg = raw_input('Message to send: ')
    publish_input(msg)
    input_message()


if __name__ == "__main__":
    websocket.enableTrace(False)
    ws = websocket.WebSocketApp("ws://localhost:9090", on_message=on_message, on_error=on_error, on_close=on_close)
    ws.on_open = on_open
    thread.start_new_thread(input_message, ())
    ws.run_forever()
