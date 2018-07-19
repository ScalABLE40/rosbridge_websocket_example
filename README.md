# ROSBridge WebSocket Example

This example comprises a ROS node and simple python program that can communicate over a rosbridge websocket implementation.

## Table of Contents

* [Installation](#installation)
* [Usage](#usage)

## <a name="installation"></a>Installation

Do a git clone to your catkin workspace. And then compile it with the command "catkin_make".

### Installing External Dependencies:

rosbridge:
```
sudo apt install ros-kinetic-rosbridge-server
```

Python websocket:
```
sudo pip install websocket-client
```


## <a name="usage"></a> Usage

### Launching the ROS node

First launch the ROS node by executing the following command:
```
roslaunch rosbridge_test run.launch
```
This launch file will launch the ROS node and the rosbridge server.


### running the python program

Using the terminal, go to the "python_websocket" directory.
To run the python program execute the following command:
```
./websocket_example.py
```

### Publish data with the ROS node

To publish data with the ROS node and receive it with the python program, it is only
needed to write the desired message on the terminal window where the ROS node
was launched and hit the enter key.

As it could be seen, the message will appear on the python program windows with
a JSON formatting. This means that the python program subscribed to the ROS topic
and received it with no problems.

### Publish data with the python program

To publish data with the python program, the process is the same as the ROS
node: just write the desired message on the terminal window of the python
program and hit the enter key.

The string will be received by the ROS node and that information will appear on its respective terminal window.
